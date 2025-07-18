import os
import django

# Set up environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project_name.settings')  # Replace with your actual project name
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Query: All books by a specific author
author = Author.objects.get(name="George Orwell")
books_by_author = Book.objects.filter(author=author)
print(f"Books by {author.name}: {[book.title for book in books_by_author]}")

# Query: List all books in a library
library = Library.objects.get(name="City Central Library")
books_in_library = library.books.all()
print(f"Books in {library.name}: {[book.title for book in books_in_library]}")

# Query: Retrieve the librarian for a library
librarian = Librarian.objects.get(library=library)
print(f"Librarian for {library.name}: {librarian.name}")

