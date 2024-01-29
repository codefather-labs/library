"""
There is not enough time to build a full-fledged
flexible domain architecture, so it was done in haste
"""

import abc
from typing import List, Iterable

from apps.library.models import Book, Author
from apps.rent.models import Rent


class ILibraryService(abc.ABC):
    @abc.abstractmethod
    def get_all_books(self, fields: list = None) -> Iterable[Book]: ...

    @abc.abstractmethod
    def get_book_by_id(
            self, book_id: int
    ) -> Book: ...

    @abc.abstractmethod
    def get_author_by_name(
            self, author_name: str
    ) -> Author: ...

    @abc.abstractmethod
    def get_books_by_author_id(
            self, author_id: int
    ) -> Iterable[Book]: ...


class IRentService:

    @abc.abstractmethod
    def get_all_rent(
            self, fields: list = None
    ) -> Iterable[Rent]: ...

    @abc.abstractmethod
    def get_rent_by_id(
            self, rent_id: int
    ) -> Rent:
        ...

    @abc.abstractmethod
    def get_rent_by_client_phone(
            self, client_phone: str
    ) -> Rent: ...


class IServiceManager(abc.ABC):
    @abc.abstractmethod
    def get_library_service(self) -> ILibraryService: ...

    @abc.abstractmethod
    def get_rent_service(self) -> IRentService: ...
