from django.urls import path

from account import views
urlpatterns = [
    path('acces', views.acces, name='acces'),
    path('inscription', views.inscription, name='inscription'),

    path('acceuil', views.acceuil, name='acceuil'),

    path('logout',views.logoutUser,name='logout'),
    ]