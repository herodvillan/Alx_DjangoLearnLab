from django.shortcuts import rende, redirect
from django.views.generic.detail import DetailView
from .models import Book, Library
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import views as auth_views


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form}

# Function-Based View (strict match)
def list_books(request):
    books = Book.objects.all()  # exact requirement
    return render(request, 'relationship_app/list_books.html', {'books': books})  # exact template path

# Class-Based View
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

