from django.shortcuts import render, redirect, get_object_or_404
from .models import BorrowedBook, ReturnedBook, Book
from book_management.models import Book
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def borrow_return(request):
    if not request.user.is_authenticated:
        return redirect('login')

    borrowed_books = BorrowedBook.objects.filter(user=request.user)
    
    context = {
        'borrowed_books': borrowed_books
    }

    return render(request, 'borrow_return/borrow_return.html', context)

def borrow_book(request, book_id):
    if not request.user.is_authenticated:
        messages.error(request, 'You need to be logged in to borrow a book.')
        return redirect('login')
    
    book = get_object_or_404(Book, id=book_id)

    if book.quantity <= 0:
        messages.error(request, 'Sorry, this book is not available for borrowing at the moment.')
        return redirect('book_store') 

    book.quantity -= 1
    book.save()

    BorrowedBook.objects.create(user=request.user, book=book)

    messages.success(request, 'You have successfully borrowed the book!')
    return redirect('borrow_return')

def borrow_return_view(request):
    return render(request, 'borrow_return/borrow_return.html')

@login_required  
def borrow_book(request, book_id):
    book = Book.objects.get(pk=book_id)
    if book.availability_status > 0:
        if not BorrowedBook.objects.filter(user=request.user, book=book).exists():
            BorrowedBook.objects.create(user=request.user, book=book)
            book.availability_status -= 1
            book.save()
    return redirect('book_detail', category_slug=book.genre.slug, book_slug=book.slug)

@login_required
def return_book(request, book_id):
    book = Book.objects.get(pk=book_id)
    if BorrowedBook.objects.filter(user=request.user, book=book).exists():
        BorrowedBook.objects.filter(user=request.user, book=book).delete()
        ReturnedBook.objects.create(user=request.user, book=book, review=request.POST['review'])
        book.availability_status += 1
        book.save()
    return redirect('book_detail', category_slug=book.genre.slug, book_slug=book.slug)