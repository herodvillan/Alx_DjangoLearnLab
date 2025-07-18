from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Book, Library
from .models import Library

# Function-Based View (strict match)
def list_books(request):
    books = Book.objects.all()  # exact requirement
    return render(request, 'relationship_app/list_books.html', {'books': books})  # exact template path

# Class-Based View
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

