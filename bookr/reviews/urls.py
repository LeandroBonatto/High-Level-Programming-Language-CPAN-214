from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
                path('', views.welcome_view, name='Welcome View'),
                path('int:id>/', views.welcome_view_book, name='Welcome View Book'),
                path('books/', views.book_list, name='Books List'),]