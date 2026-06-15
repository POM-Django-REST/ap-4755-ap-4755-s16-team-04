from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from .forms import OrderCreateForm, OrderEditForm
from .models import Order
from book.models import Book


def orders_list(request):
    orders = Order.objects.all()
    return render(request, "order/list.html", {"orders": orders})


@login_required
def my_orders(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, "order/my_orders.html", {"orders": orders})


def user_orders(request, user_id):
    orders = Order.objects.filter(user_id=user_id)
    return render(request, "order/list.html", {"orders": orders})


@login_required
def create_order(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            Order.create(
                user=request.user,
                book=book,
                plated_end_at=form.cleaned_data['plated_end_at']
            )
            return redirect('my_orders')
    else:
        form = OrderCreateForm()

    return render(request, 'order/order_form.html', {'form': form, 'book': book})


@login_required
def edit_order(request, id):
    order = get_object_or_404(Order, id=id)

    if request.method == 'POST':
        form = OrderEditForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('orders_list')
    else:
        form = OrderEditForm(instance=order)

    return render(request, 'order/order_form.html', {'form': form, 'order': order})


@login_required
def close_order(request, id):
    order = Order.get_by_id(id)

    if order:
        order.update(end_at=timezone.now())
        order.book.count += 1
        order.book.save()

    return redirect('orders_list')