import factory
import factory.fuzzy
from factory.django import DjangoModelFactory

from .models import TableRow


class TableRowFactory(DjangoModelFactory):
    class Meta:
        model = TableRow

    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    home_state = factory.fuzzy.FuzzyChoice(['NE', 'IA', 'SD', 'CA', 'IL', 'FL', 'WA'])
    age = factory.Faker('random_int', min=18, max=99, step=1)
