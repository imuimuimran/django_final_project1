from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from wishlist.models import WishlistItem
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import WishlistItem

# Create your views here.

@login_required
def user_wishlist(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    wishlist_items = WishlistItem.objects.filter(user=request.user)

    context = {
        'wishlist_items': wishlist_items
    }

    return render(request, 'wishlist/wishlist.html', context) 


def add_to_wishlist(request, book_id):
    book = get_object_or_404(Book, id=book_id)  

    if WishlistItem.objects.filter(book=book, user=request.user).exists():
        messages.warning(request, 'Book is already in your wishlist.')
    else:
        wishlist_item = WishlistItem(book=book, user=request.user)
        wishlist_item.save()
        messages.success(request, 'Book added to your wishlist.')

    return redirect('wishlist')   

