from django.contrib import admin
from .models import Category, Paste


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


@admin.register(Paste)
class PasteAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'text')
