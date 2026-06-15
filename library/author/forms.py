from django import forms
from .models import Author

class AuthorForm(forms.ModelForm):

    patronymic = forms.CharField(
        label="По батькові (необов'язково)",
        required=False,  # ТУТ САМА СУТЬ
        widget=forms.TextInput(attrs={'placeholder': "Введіть по батькові"})
    )

    class Meta:
        model = Author
        fields = ['name', 'surname', 'patronymic']
        labels = {
            'name': "Ім'я",
            'surname': "Прізвище",
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': "Введіть ім'я"}),
            'surname': forms.TextInput(attrs={'placeholder': "Введіть прізвище"}),
        }