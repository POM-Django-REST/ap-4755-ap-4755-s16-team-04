from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import CustomUser
from .forms import RegisterForm, LoginForm  # Наші нові форми

# ---- Нові імпорти для Django REST Framework (Спринт 16) ----
from rest_framework import viewsets
from .serializers import UserSerializer
# ------------------------------------------------------------

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = CustomUser.objects.create_user(
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                role=int(form.cleaned_data['role'])
            )
            login(request, user)
            return redirect('dashboard')
    else:
        form = RegisterForm()

    return render(request, 'authentication/register.html', {'form': form})


def login_view(request):
    error = None
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email_input = form.cleaned_data['email']
            password_input = form.cleaned_data['password']

            user = authenticate(request, username=email_input, password=password_input)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                error = "Невірний Email або пароль."
    else:
        form = LoginForm()

    return render(request, 'authentication/login.html', {'form': form, 'error': error})


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def dashboard_view(request):
    return render(request, 'authentication/dashboard.html')




class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()  # Пряме і правильне звернення до вашої моделі
    serializer_class = UserSerializer