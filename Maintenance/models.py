from __future__ import unicode_literals

from django.db import models

# Create your models here.
class PreRegistrations(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    block_name = models.CharField(max_length=50)
    flat_number = models.CharField(max_length=50)
    mobile_number = models.CharField(max_length=50)
    email_id = models.CharField(max_length=50)
    type_occupancy = models.BooleanField()
    apartment_id = models.CharField(max_length=50)