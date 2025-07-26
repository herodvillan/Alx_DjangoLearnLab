from django.contrib.auth.decorators import permission_required
from django.shortcuts import render
from .models import Profile, Book
from .forms import ExampleForm

@permission_required('relationship_app.view_book', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/book_list.html', {'books': books})


@permission_required('accounts.can_view', raise_exception=True)
def view_profile(request):
    profiles = Profile.objects.all()
    return render(request, 'accounts/view_profile.html', {'profiles': profiles})

@permission_required('accounts.can_create', raise_exception=True)
def create_profile(request):
    # Form handling logic
    return render(request, 'accounts/create_profile.html')

@permission_required('accounts.can_edit', raise_exception=True)
def edit_profile(request, pk):
    # Edit logic
    return render(request, 'accounts/edit_profile.html')

@permission_required('accounts.can_delete', raise_exception=True)
def delete_profile(request, pk):
    # Delete logic
    return render(request, 'accounts/delete_profile.html')


# Create your views here.
