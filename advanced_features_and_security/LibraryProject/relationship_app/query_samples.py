import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')  # Change 'LibraryProject' to your actual project name
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Variables for querying
author_name = "George Orwell"
library_name = "City Central Library"

# 1. Query all books by a specific author
try:
    author = Author.objects.get(name=author_name)
    books_by_author = Book.objects.filter(author=author)
    print(f"Books by {author.name}: {[book.title for book in books_by_author]}")
except Author.DoesNotExist:
    print(f"Author '{author_name}' not found.")

# 2. List all books in a library
try:
    library = Library.objects.get(name=library_name)
    books_in_library = library.books.all()
    print(f"Books in {library.name}: {[book.title for book in books_in_library]}")
except Library.DoesNotExist:
    print(f"Library '{library_name}' not found.")

# 3. Retrieve the librarian for a library
try:
    librarian = Librarian.objects.get(library=library)
    print(f"Librarian for {library.name}: {librarian.name}")
except Librarian.DoesNotExist:
    print(f"No librarian found for library '{library_name}'.")

