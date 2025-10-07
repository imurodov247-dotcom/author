from django.contrib import admin
from . import models
from .models import Book


# Register your models here.
@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['name','author','yil']
    list_editable = ['author']
    search_fields = ['name']
    list_filter = ['author']