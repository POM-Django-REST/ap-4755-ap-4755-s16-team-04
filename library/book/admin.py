from django.contrib import admin
from .models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'count', 'display_authors')


    list_filter = ('id', 'name', 'authors')


    fieldsets = (

        ('Інформація про книгу (Незмінна)', {
            'fields': ('name', 'authors'),
            'description': 'Основні бібліографічні дані, які залишаються постійними.'
        }),

        ('Динамічні дані (Змінна)', {
            'fields': ('count', 'description'),
            'description': 'Параметри, що можуть редагуватися (кількість у наявності, опис тощо).'
        }),
    )


    def display_authors(self, obj):
        return ", ".join([f"{author.name} {author.surname}" for author in obj.authors.all()])


    display_authors.short_description = 'Автори'
