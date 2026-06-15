from django.contrib import admin
from .models import Author

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):

    list_display = ('id', 'surname', 'name', 'patronymic')


    ordering = ('surname', 'name')


    fields = ('surname', 'name', 'patronymic')


    search_fields = ('surname', 'name')
