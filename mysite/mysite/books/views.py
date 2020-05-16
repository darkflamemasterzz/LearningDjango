from django.template.loader import render_to_string
from django.http import HttpResponse
from mysite.books.models import Book

from django.shortcuts import render

def search_form(request):
    renderer =  render_to_string('search_form.html')
    return HttpResponse(renderer)

def search(request):
    if 'q' in request.GET:
        q = request.GET['q']
        books = Book.objects.filter(title__contains=q)
        renderer = render_to_string('search_results.html', {'books':books, 'query':q})
    else:
        renderer = 'Please submit a search item'
    return HttpResponse(renderer)
