from django.urls import path
from . import views
from .views import borrow_return

urlpatterns = [
    path('borrow_return/', borrow_return, name='borrow_return'),
    path('borrow_return/', views.borrow_return_view, name='borrow_return'),
    path('borrow/<int:book_id>/', views.borrow_book, name='borrow_book'),
    path('return/<int:book_id>/', views.return_book, name='return_book'),
    path('borrow_book/<int:book_id>/', views.borrow_book, name='borrow_book'),
    path('borrow_return/borrow/<int:book_id>/', views.borrow_book, name='borrow_book'),
]


