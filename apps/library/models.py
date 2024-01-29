from django.db import models

from apps.core.mixins import TimestampMixin, NameMixin


class Author(NameMixin,
             TimestampMixin):
    ...


class Book(NameMixin,
           TimestampMixin):
    """
    M2M relations creates indexes on "through" table by default.
        > see sqlmigrations/library_0001.sql

    retrieve: python3 manage.py sqlmigrate library 0001
    """
    description = models.TextField()
    authors = models.ManyToManyField(
        "library.Author",
        null=False,
        related_name="books",
    )
    is_available = models.BooleanField(
        default=True
    )
