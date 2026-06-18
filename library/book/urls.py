from django.urls import path
from .views import BookListView, BookDetailView

urlpatterns = [
    path('', BookListView.as_view()),
    path('<int:book_id>/', BookDetailView.as_view()),
]