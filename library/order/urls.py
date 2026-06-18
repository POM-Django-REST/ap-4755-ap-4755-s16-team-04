from django.urls import path
from .views import OrderListView, OrderDetailView

urlpatterns = [
    path('', OrderListView.as_view()),
    path('user/<int:user_id>/order/<int:order_id>/', OrderDetailView.as_view()),
]
