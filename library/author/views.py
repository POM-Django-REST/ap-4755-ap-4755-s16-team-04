from django.shortcuts import render, redirect, get_object_or_404
from .models import Author
from .forms import AuthorForm

def authors_list_view(request):
    authors = Author.objects.all()
    return render(request, 'author/authors_list.html', {'authors': authors})

def author_create_view(request):

    if not request.user.is_authenticated or (
            not request.user.is_superuser and getattr(request.user, 'role', None) != 1):
        return redirect('login')

    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('authors_list')
    else:
        form = AuthorForm()

    return render(request, 'author/author_form.html', {'form': form})

def author_delete_view(request, author_id):
    if not request.user.is_authenticated or (
            not request.user.is_superuser and getattr(request.user, 'role', None) != 1):
        return redirect('login')

    author = get_object_or_404(Author, id=author_id)

    if request.method == 'POST':
        if author.book_set.exists():
            return redirect('authors_list')
        author.delete()
        return redirect('authors_list')

    return render(request, 'author/author_confirm_delete.html', {'author': author})

def author_edit_view(request, author_id):
    if not request.user.is_authenticated or (
            not request.user.is_superuser and getattr(request.user, 'role', None) != 1):
        return redirect('login')

    author = get_object_or_404(Author, id=author_id)

    if request.method == 'POST':

        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
            return redirect('authors_list')
    else:

        form = AuthorForm(instance=author)


    return render(request, 'author/author_form.html', {'form': form, 'author': author})

