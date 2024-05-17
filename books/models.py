from django.db import models


class BookModel(models.Model):
    image = models.ImageField(upload_to='books-images', null=True)
    author = models.CharField(max_length=128)
    title = models.CharField(max_length=255)
    info = models.TextField()
    pages = models.IntegerField()
    ebook = models.FileField(upload_to='ebooks', null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title

    class Meta:
        verbose_name = 'book'
        verbose_name_plural = 'books'
