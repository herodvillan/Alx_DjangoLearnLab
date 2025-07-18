from django.urls import path
from . import views
from .views import list_books
urlpatterns = [
    path('books/', views.list_books, name='list_books'),  # function-based
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),  # class-based
]

