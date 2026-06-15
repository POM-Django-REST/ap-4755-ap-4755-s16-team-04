from django.urls import path
from . import views

urlpatterns = [
    path("", views.books_list, name="books_list"),

    path("create/", views.book_create, name="book_create"),

    path("<int:id>/", views.book_detail, name="book_detail"),

    path("<int:id>/edit/", views.book_edit, name="book_edit"),

    path("user/<int:user_id>/", views.user_books, name="user_books"),
]