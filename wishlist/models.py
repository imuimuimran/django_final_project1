from django.db import models
from book_management.models import Book 
from django.contrib.auth.models import User
    
class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    books = models.ManyToManyField(Book, related_name='wishlists')

    def __str__(self):
        return f'Wishlist for {self.user.username}'

class WishlistItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)  

    def __str__(self):
        return f'{self.user.username}\'s wishlist item for {self.book.title}'
