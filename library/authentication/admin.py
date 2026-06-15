from django.contrib import admin
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):

    list_display = ('id', 'email', 'first_name', 'last_name', 'role', 'is_active')


    list_filter = ('role', 'is_active')


    search_fields = ('email', 'first_name', 'last_name')


    fieldsets = (
        ('Облікові дані', {
            'fields': ('email', 'password')
        }),
        ('Особиста інформація', {
            'fields': ('first_name', 'last_name')
        }),
        ('Права доступу та статус', {
            'fields': ('role', 'is_active'),
            'description': 'Роль: 0 — Звичайний користувач (Гість), 1 — Бібліотекар/Адмін.'
        }),
    )