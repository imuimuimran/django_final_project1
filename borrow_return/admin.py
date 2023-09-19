from django.contrib import admin
from .models import BorrowedBook, ReturnedBook

# Register your models here.

admin.site.register(BorrowedBook)
admin.site.register(ReturnedBook)