from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.rent.models import Rent


@receiver(post_save, sender=Rent, dispatch_uid="update_book_status")
def update_book_status(sender, instance: Rent, **kwargs):
    """
    This is an anti-pattern for DDD, but for our purposes it will do
    """
    if instance.status == Rent.RETURNED:
        instance.book.is_available = True
    else:
        instance.book.is_available = False

    instance.book.save()
