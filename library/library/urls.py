from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('authentication.urls')),
    path('users/', include('users.urls')),
    path('authors/', include('author.urls')),
    path('api/v1/book/', include('book.urls')),
    path('api/v1/order/', include('order.urls')),


    path('', RedirectView.as_view(url='books/', permanent=False)),
]