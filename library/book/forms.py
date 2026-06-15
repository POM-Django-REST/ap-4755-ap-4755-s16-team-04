from django import forms
from .models import Book


class BookSearchForm(forms.Form):
    title = forms.CharField(required=False)
    author = forms.CharField(required=False)


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'description', 'count', 'authors']