from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from .utils import *


# Create your views here.
def index(request):
    return HttpResponse('Hello, world!')


def index(request):
    name = request.GET.get('name') or 'World!!!'
    return HttpResponse('Hello, {}!'.format(name))


def index(request):
    return render(request, 'base_old.html')


def index(request):
    n = 'world'
    return render(request, 'base_old.html', {'name': n})


def welcome_view(request):
    message = f'<html>' \
              f'<h1>Welcome to Bookr!</h1>' \
              f'<p>{Book.objects.count()} books and counting!</p>' \
              f'</html>'
    return HttpResponse(message)


def welcome_view_book(request, id):
    book = Book.objects.get(id=id)
    message = f"You have selected the  {book.title} book!"
    return HttpResponse(message)


def welcome_view(request):
    count = Book.objects.count()
    return render(request, 'base_old.html', {'book_counts': count})


def book_list(request):
    books = Book.objects.all()
    books_list = []
    for book in books:
        reviews = book.review_set.all()
        if reviews:
            book_rating = average_rating([review.rating for review in reviews])
            number_of_reviews = len(reviews)
        else:
            book_rating = None
            number_of_reviews = 0
        books_list.append({'book': book, 'book_rating': book_rating, 'number_of_reviews': number_of_reviews})
    context = {'book_list': books_list}
    # return render(request, 'books_list.html', context)
    return render(request, 'base_extended.html', context)
