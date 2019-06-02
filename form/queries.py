from .models import Entry


def latest_entries():
    return Entry.objects.order_by('-id')[:10]
