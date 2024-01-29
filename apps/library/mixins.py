class RentBookStatusMixin:
    RENTED = 'rented'
    RETURNED = 'returned'
    # we could make this OVERDUE status useful in the future
    # if we used celery-beat with a daily cron
    # checking all the books
    OVERDUE = 'overdue'

    STATUSES = (
        (RENTED, RENTED),
        (RETURNED, RETURNED),
        (OVERDUE, OVERDUE)
    )
