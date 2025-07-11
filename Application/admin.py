from django.contrib import admin
from .models import Book, HindiVersion



# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'summary','bookPDF_url')
    search_fields = ('title', 'author')
    list_filter = ('author',)
    ordering = ('title',)

@admin.register(HindiVersion)
class HindiVersionAdmin(admin.ModelAdmin):
    list_display = ('hindi_title', 'hindi_author', 'hindi_summary')
    search_fields = ('hindi_title', 'hindi_author')
    list_filter = ('hindi_author',)
    ordering = ('hindi_title',)
