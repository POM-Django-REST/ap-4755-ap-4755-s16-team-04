from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q

from .models import Book
from order.models import Order
from .forms import BookSearchForm, BookForm


def books_list(request):
    books = Book.objects.all()

    form = BookSearchForm(request.GET)
    if form.is_valid():
        title = form.cleaned_data['title']
        author = form.cleaned_data['author']

        if title:
            books = books.filter(name__icontains=title)

        if author:
            words = author.split()
            author_filter = Q()
            for word in words:
                author_filter &= (
                    Q(authors__name__icontains=word) |
                    Q(authors__surname__icontains=word)
                )
            books = books.filter(author_filter).distinct()

    return render(request, "book/list.html", {"books": books, "form": form})


def book_detail(request, id):
    book = Book.get_by_id(id)
    return render(request, "book/detail.html", {"book": book})


def user_books(request, user_id):
    orders = Order.objects.filter(user_id=user_id, end_at=None)
    books = [order.book for order in orders]
    return render(request, "book/user_books.html", {"books": books})


def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('books_list')
    else:
        form = BookForm()
    return render(request, 'book/book_form.html', {'form': form})


def book_edit(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_detail', id=book.id)
    else:
        form = BookForm(instance=book)
    return render(request, 'book/book_form.html', {'form': form, 'book': book})