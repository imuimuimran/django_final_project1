from django.db import models
from book_management.models import Book
from django.contrib.auth.models import User

class BorrowedBook(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrowed_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} borrowed {self.book.title}'

class ReturnedBook(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    returned_date = models.DateTimeField(auto_now_add=True)
    review = models.TextField()

    def __str__(self):
        return f'{self.user.username} returned {self.book.title}'

