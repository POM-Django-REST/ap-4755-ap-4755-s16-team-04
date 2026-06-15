from django.urls import path
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),


    path('', RedirectView.as_view(url='login/', permanent=False)),
]