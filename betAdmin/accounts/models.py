from django.contrib.auth.models import User
from django.db import models


class Profile(User):

    phone = models.CharField(max_length=20, blank=True, null=True)
    country = models.CharField(max_length=20, blank=True, null=True)
    city = models.CharField(max_length=20, blank=True, null=True)
    zip_code = models.CharField(max_length=20, blank=True, null=True)
    street_address = models.CharField(max_length=50, blank=True, null=True)    
    uf = models.CharField(max_length=2, blank=True, null=True)    
    number = models.CharField(max_length=5, blank=True, null=True)    
    email_confirmed = models.BooleanField(default=False)


class Query(models.Model):

    name = models.CharField(max_length=50)
    query = models.CharField(max_length=250)
    profile = models.ForeignKey(Profile, related_name='query', on_delete=models.CASCADE)