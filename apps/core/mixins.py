from django.db import models
from django.utils import timezone


class TimestampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class DatetimeRangeMixin(models.Model):
    time_from = models.DateTimeField(
        db_index=True,
        null=False,
        default=timezone.now
    )
    time_to = models.DateTimeField(
        db_index=True,
        null=False,
        default=None
    )

    class Meta:
        abstract = True


class NameMixin(models.Model):
    name = models.CharField(max_length=255, db_index=True)

    class Meta:
        abstract = True
