from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from rest_framework.routers import DefaultRouter
from author.views import AuthorViewSet
from authentication.views import UserViewSet


router = DefaultRouter()
router.register(r'author', AuthorViewSet, basename='author')
router.register(r'user', UserViewSet, basename='user')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('authentication.urls')),
    path('users/', include('users.urls')),
    path('authors/', include('author.urls')),
    path('api/v1/book/', include('book.urls')),
    path('api/v1/order/', include('order.urls')),


    path('api/v1/', include(router.urls)),

    path('', RedirectView.as_view(url='books/', permanent=False)),
]