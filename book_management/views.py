from django.shortcuts import render, get_object_or_404, redirect
from .models import Book, Review
from .forms import ReviewForm
from borrow_return.models import BorrowedBook
from category.models import Category
from django.core.paginator import Paginator
from django.db.models import Q
from wishlist.models import Wishlist
from django.contrib import messages

# Create your views here.

def book_store(request, category_slug=None):
    books = Book.objects.filter(availability_status=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        books = books.filter(genre=category)
        page = request.GET.get('page')
        paginator = Paginator(books, 3) 
        paged_book = paginator.get_page(page)
        
    else:
        paginator = Paginator(books, 6)
        page = request.GET.get('page')
        paged_book = paginator.get_page(page)
        
        for i in paged_book:
            print(i)
        print(paged_book.has_next(), paged_book.has_previous(), paged_book.previous_page_number, paged_book.next_page_number)

    categories = Category.objects.all()
    context = {'books': paged_book, 'categories': categories}
    return render(request, 'book_management/book_store.html', context)

def book_detail(request, category_slug, book_slug):
    single_book = get_object_or_404(Book, slug=book_slug, genre__slug=category_slug)

    if request.user.is_authenticated:
        in_wishlist = Wishlist.objects.filter(user=request.user, books=single_book).exists()
    else:
        in_wishlist = False

    if request.method == 'POST':
        if not in_wishlist:  
            wishlist, created = Wishlist.objects.get_or_create(user=request.user)
            wishlist.books.add(single_book)
        else:  
            wishlist = Wishlist.objects.get(user=request.user)
            wishlist.books.remove(single_book)
            
    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.user = request.user
            review.book = single_book
            review.save()

            single_book.no_of_books_available += 1
            single_book.save()

            BorrowedBook.objects.filter(user=request.user, book=single_book).delete()

            messages.success(request, 'You have successfully returned the book and reviewed it!')

        return redirect('book_detail', category_slug=category_slug, book_slug=book_slug)
    else:
        review_form = ReviewForm()

    return render(request, 'book_management/book_detail.html', {'book': single_book,'in_wishlist': in_wishlist, 'review_form': ReviewForm()})

def book_search(request):
    query = request.GET.get('q')
    if query:
        books = Book.objects.filter(Q(title__icontains=query) & Q(availability_status=True))
        categories = Category.objects.all()
        context = {'books': books, 'categories': categories}
    else:
        context = {'books': [], 'categories': Category.objects.all()}
    
    return render(request, 'book_management/book_search.html', context) 

def borrow_book(request, book_id):
    if not request.user.is_authenticated:
        messages.error(request, 'You need to be logged in to borrow a book.')
        return redirect('login')
    
    book = get_object_or_404(Book, id=book_id)

    if book.no_of_books_available <= 0:
        messages.error(request, 'Sorry, this book is not available for borrowing at the moment.')
        return redirect('book_store')  

    book.no_of_books_available -= 1
    book.save()

    BorrowedBook.objects.create(user=request.user, book=book)

    messages.success(request, 'You have successfully borrowed the book!')
    
    return redirect('book_detail', category_slug=book.genre.slug, book_slug=book.slug)

def return_book(request, book_id):
    if not request.user.is_authenticated:
        messages.error(request, 'You need to be logged in to return a book.')
        return redirect('login')

    book = get_object_or_404(Book, id=book_id)


    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.user = request.user 
            review.book = book
            review.save()
    
    book.no_of_books_available += 1
    book.save()

    messages.success(request, 'You have successfully returned the book and reviewed it!')
    return redirect('book_detail', category_slug=book.genre.slug, book_slug=book.slug)