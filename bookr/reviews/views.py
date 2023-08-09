from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse('base.html')

def index(request):
    name = request.GET.get('name') or 'World!!!'
    return HttpResponse('Hello, {}!'.format(name))

def index(request):
    return render(request, 'base.html')

def index(request):
    n = 'world'
    return render(request, 'base.html', {'name': n})

def book_search(request):
    search_text = request.GET.get('search_text')
    return render(request, 'search-results.html')
