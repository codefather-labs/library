import datetime
from typing import Iterable

from django.db.models import Case, When, Value, BooleanField

from apps.rent.models import Rent
from services.interfaces import IRentService


class DjangoInlineRentService(IRentService):
    def get_all_rent(self, fields: list = None) -> Iterable[Rent]:
        query = Rent.objects.prefetch_related(
            "book", "book__authors"
        ).annotate(
            is_overdue=Case(
                When(
                    time_to__lte=datetime.datetime.now(
                        tz=datetime.timezone.utc
                    ),
                    then=True
                ),
                default=Value(False, output_field=BooleanField()),
            ),
        )

        # if fields:
        #     query = query.only(*fields)
        return query.all()

    def get_rent_by_id(self, rent_id: int) -> Rent:
        pass

    def get_rent_by_client_phone(self, client_phone: str) -> Rent:
        pass
