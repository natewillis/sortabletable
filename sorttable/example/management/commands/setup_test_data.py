from django.db import transaction
from django.core.management.base import BaseCommand

from example.models import TableRow
from example.factories import TableRowFactory

NUM_ENTRIES = 1000


class Command(BaseCommand):
    help = "Generates test data"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting old data...")
        models = [TableRow]
        for m in models:
            m.objects.all().delete()

        self.stdout.write("Creating new data...")
        # Create all the users
        rows = []
        for _ in range(NUM_ENTRIES):
            row = TableRowFactory()