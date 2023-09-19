from django.urls import path
from . import views
from .views import borrow_book

urlpatterns = [
    path('book_store/', views.book_store, name='book_store'),   
    path('book_store/<str:category_slug>/', views.book_store, name='book_store'),
    path('book_detail/<str:category_slug>/<str:book_slug>/', views.book_detail, name='book_detail'),
    path('book_management/book_detail/<str:category_slug>/<str:book_slug>/', views.book_detail, name='book_by_category'),
    path('book_search/', views.book_search, name='book_search'),
    path('borrow/<int:book_id>/', views.borrow_book, name='borrow_book'),
    path('return/<int:book_id>/', views.return_book, name='return_book'),
]

