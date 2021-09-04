from django.db import models


# Create your models here.
class TableRow(models.Model):
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    home_state = models.CharField(max_length=2, blank=True)
    age = models.IntegerField(null=False)
