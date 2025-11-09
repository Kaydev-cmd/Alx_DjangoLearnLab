import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def get_books_by_author(author_name):
    books = Book.objects.filter(author__name=author_name)
    print(f"Books by {author_name}:")
    for book in books:
        print(f"- {book.title}")
    
def get_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        print(f"Books in {library_name}:")
        for book in books:
            print(f"- {book.title} by {book.author.name}")
    except Library.DoesNotExist:
        print("Library not found.")

def get_librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = library.librarian
        return librarian
    except Library.DoesNotExist:
        return None
    except Librarian.DoesNotExist:
        return None
    
if __name__ == "__main__":
    get_books_by_author("J.K. Rowling")
    get_books_in_library("Central Library")
    librarian = get_librarian_for_library("Central Library")
    if librarian:
        print(f"Librarian for Central Library: {librarian.name}")
    else:
        print("Librarian not found for Central Library.")

