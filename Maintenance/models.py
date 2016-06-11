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
    
class UnmatchedRegistrations(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    block_name = models.CharField(max_length=50)
    flat_number = models.CharField(max_length=50)
    mobile_number = models.CharField(max_length=50, primary_key = True)
    email_id = models.CharField(max_length=50)
    type_occupancy = models.BooleanField()
    have_car = models.BooleanField()
    apartment_id = models.CharField(max_length=50)
    passwordHash = models.CharField(max_length=50)
    
class RegisteredApartUser(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    block_name = models.CharField(max_length=50)
    flat_number = models.CharField(max_length=50)
    mobile_number = models.CharField(max_length=50, primary_key = True)
    email_id = models.CharField(max_length=50)
    type_occupancy = models.BooleanField()
    have_car = models.BooleanField()
    apartment_id = models.CharField(max_length=50)
    passwordHash = models.CharField(max_length=50)
    otp_hash = models.CharField(max_length=50)
    verified_mobile = models.BooleanField()
    
class ApartmentAccount(models.Model):
    AppartmentName = models.CharField(max_length=50)
    AppartmentEmail = models.CharField(max_length=50)
    AppartmentAddress = models.CharField(max_length=500)
    NoOfBlocks = models.CharField(max_length=10)
    NumberOfFlats = models.CharField(max_length=10)
    EmailAddress = models.CharField(max_length=50)
    MobileNumber = models.CharField(max_length=15)
    LandLine = models.CharField(max_length=15)
    PasswordHash = models.CharField(max_length=50)
    AccountHolderName = models.CharField(max_length=50)
    AccountNumber = models.CharField(max_length=30)
    IFSCCode = models.CharField(max_length=20)
