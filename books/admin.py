from django.contrib import admin
from books.models import BookModel


@admin.register(BookModel)
class BookModelAdmin(admin.ModelAdmin):
    list_display = ['author', 'title', 'pages', 'created_at']
    search_fields = ['title']
    list_filter = ['created_at', 'author']
