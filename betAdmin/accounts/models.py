from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(User):
    phone = models.CharField(max_length=20, blank=True, null=True)
    country = models.CharField(max_length=20, blank=True, null=True)
    city = models.CharField(max_length=20, blank=True, null=True)
    zip_code = models.CharField(max_length=20, blank=True, null=True)
    street_address = models.CharField(max_length=50, blank=True, null=True)    
    email_confirmed = models.BooleanField(default=False)
