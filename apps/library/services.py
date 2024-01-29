from typing import List, Iterable

from django.db.models import QuerySet

from apps.library.models import Book, Author
from services.interfaces import ILibraryService


class DjangoInlineLibraryService(ILibraryService):
    def get_all_books(self, fields: list = None) -> Iterable[Book]:
        query = Book.objects.prefetch_related(
            "authors"
        )
        if fields:
            query = query.only(*fields)
        return query.all()

    def get_book_by_id(self, book_id: int) -> Book:
        return Book.objects.get(id=book_id)

    def get_author_by_name(self, author_name: str) -> Author:
        try:
            return Author.objects.get(name=author_name)
        except Author.DoesNotExist:
            return

    def get_books_by_author_id(self, author_id: int):
        return Book.objects.prefetch_related('authors').filter(
            authors__id=author_id
        )
