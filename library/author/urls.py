from django.urls import path
from .views import authors_list_view, author_create_view, author_delete_view

urlpatterns = [
    path('', authors_list_view, name='authors_list'),
    path('create/', author_create_view, name='author_create'),
    path('<int:author_id>/delete/', author_delete_view, name='author_delete'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.authors_list_view, name='authors_list'),
    path('create/', views.author_create_view, name='author_create'),
    path('<int:author_id>/edit/', views.author_edit_view, name='author_edit'),  # Новий маршрут
    path('<int:author_id>/delete/', views.author_delete_view, name='author_delete'),
]