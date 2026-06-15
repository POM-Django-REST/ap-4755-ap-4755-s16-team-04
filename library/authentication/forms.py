from django import forms
from .models import CustomUser


class RegisterForm(forms.Form):
    ROLE_CHOICES = (
        (0, 'Гість (Читач)'),
        (1, 'Бібліотекар'),
    )

    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'example@email.com'})
    )
    password = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Введіть пароль'})
    )
    first_name = forms.CharField(
        label="Ім'я",
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Ваше ім'я"})
    )
    last_name = forms.CharField(
        label="Прізвище",
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ваше прізвище'})
    )
    role = forms.ChoiceField(
        label="Роль у системі",
        choices=ROLE_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    # Валідація унікальності Email через clean-метод Django
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("Користувач з таким Email вже існує.")
        return email


class LoginForm(forms.Form):
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'example@email.com'})
    )
    password = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Введіть пароль'})
    )