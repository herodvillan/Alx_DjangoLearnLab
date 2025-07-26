##  3. `update.md`

```markdown
# Update Book Title

```python
from bookshelf.models import Book
book = Book.objects.get(title="1984")  # or "Nineteen Eighty-Four" depending on previous state
book.title = "Nineteen Eighty-Four"
book.save()
book.title
