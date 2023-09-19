from django.contrib import admin
from . models import Book
# Register your models here.

class BookAdmin(admin.ModelAdmin):
     list_display = ['title', 'author', 'genre', 'description', 'no_of_books_available' ,'publication_date', 'availability_status']
     
     prepopulated_fields = {'slug' : ('title',)}
     
admin.site.register(Book, BookAdmin)
    

    