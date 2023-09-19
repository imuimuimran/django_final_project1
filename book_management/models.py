from django.db import models
from category.models import Category
from django.contrib.auth.models import User
# Create your models here.
    
class Book(models.Model):
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.CharField(max_length=255)
    description = models.TextField(max_length=500, blank=True) 
    isbn = models.CharField(max_length=17)
    image = models.ImageField(upload_to='photos/books')
    publication_date = models.DateTimeField(auto_now_add=True)
    availability_status = models.BooleanField(default=True)
    no_of_books_available = models.PositiveIntegerField(default=0)
    genre = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    review_text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.book.title} Review'