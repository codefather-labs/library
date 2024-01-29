from django.db import models

from apps.core.mixins import TimestampMixin, DatetimeRangeMixin
from apps.library.mixins import RentBookStatusMixin


class Rent(TimestampMixin,
           DatetimeRangeMixin,
           RentBookStatusMixin):
    """
    FK creates index by default
        > see sqlmigrations/rent_0001.sql

    retrieve: python3 manage.py sqlmigrate rent 0001
    """

    status = models.CharField(
        max_length=10,
        choices=RentBookStatusMixin.STATUSES,
        default=RentBookStatusMixin.RENTED
    )
    book = models.ForeignKey(
        "library.Book",
        on_delete=models.deletion.SET_NULL,
        null=True,
        blank=True,
    )
    client_phone = models.CharField(
        max_length=22,
        default=None,
        null=False
    )
