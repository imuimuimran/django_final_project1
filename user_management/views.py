from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth import login, logout, authenticate
from book_management.models import Book
from wishlist.models import Wishlist
from django.contrib import messages

# Create your views here.
def user_register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    return render(request, 'user_management/register.html', {'form':form})


def user_profile(request):
    if not request.user.is_authenticated:
        return redirect('login')

    wishlist, created = Wishlist.objects.get_or_create(user=request.user)

    wishlist_books = wishlist.books.all() 

    context = {
        'wishlist_books': wishlist_books
    }

    # return render(request, 'user_management/dashboard.html', context)
    return redirect('wishlist')

def user_login(request):
    if request.method == 'POST':
        user_name = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = user_name, password = password)
        if user is not None and user.is_authenticated:
            login(request, user)
            return redirect('profile')
        messages.error(request, 'Invalid username or password') 
        return redirect('login')

    return render(request, 'user_management/signin.html')

def user_logout(request):
    logout(request)
    return redirect('login')
