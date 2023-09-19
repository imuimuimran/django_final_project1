from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.user_wishlist, name='wishlist'), 
    path('wishlist/add/<int:book_id>/', views.add_to_wishlist, name='wishlist_add'),
    path('add_to_wishlist/<int:book_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('wishlist/add/<int:book_id>/', login_required(views.add_to_wishlist), name='wishlist_add'),
    path('add_to_wishlist/<int:book_id>/', login_required(views.add_to_wishlist), name='add_to_wishlist'),
]


    
