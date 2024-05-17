from django.http import HttpResponse
from django.shortcuts import render
from .models import BookModel


def books_list_view(request):
    books = BookModel.objects.all()
    q = request.GET.get('q')
    if q:
        books = books.filter(title__icontains=q)

    context = {'books': books}
    return render(request, 'books.html', context)


def book_detail_view(request, pk):
    book = BookModel.objects.filter(id=pk).first()
    if book:
        context = {'book': book}
        return render(request, 'book-detail.html', context)
    else:
        return HttpResponse('Book not found')


def download_book_view(request, pk):
    book = BookModel.objects.filter(id=pk).first()

    if book:
        file_path = str(book.ebook)
        with open(file_path, 'rb') as f:
            response = HttpResponse(f.read(), content_type='application/pdf')
            return response
    else:
        return HttpResponse("Book not found")
