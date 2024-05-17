from django.urls import path

from books.views import books_list_view, book_detail_view, download_book_view

app_name = 'books'

urlpatterns = [
    path('', books_list_view, name='list'),
    path('<int:pk>/', book_detail_view, name='detail'),
    path('download/<int:pk>/', download_book_view, name='download')
]
