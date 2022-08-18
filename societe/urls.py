from django.urls import path

from account import cart, favorite
from . import views

urlpatterns = [
    path('', views.index, name='index'),


    path('collection/<str:name>', views.collectionsviews, name='collectionsviews'),
    path('collection/<str:cat_name>/<str:ser_title>', views.serviceviews, name='serviceviews'),
    path('add-to-cart', cart.addtocart, name='addtocart'),
    path('cart', cart.viewcart, name="cart"),
    path('update-cart', cart.updatecart, name="updatecart"),
    path('delete-cart-item', cart.deletecartitem, name="deletecarteitem"),
    path('wishlist', favorite.index, name='wishlist'),
    path('add-to-wishlist', favorite.addtowishlist, name="addtowishlist"),
    path('delete-wishlist-item', favorite.deletewishlistitem, name="deletewishlistitem"),

    path('home', views.home, name='home'),
    path('<str:room>/', views.room, name='room'),
    path('checkview', views.checkview, name='checkview'),
    path('send', views.send, name='send'),
    path('getMessages/<str:room>/', views.getMessages, name='getMessages')

]