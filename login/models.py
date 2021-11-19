from django.db import models

from django.contrib.auth.models import AbstractUser 

# Create your models here.
class User(AbstractUser):
    affiliation = models.CharField(max_length=255, default='')
    phone = models.CharField(max_length=255, default='')
    address = models.CharField(max_length=255, default='')
    #groups = models.ManyToManyField(Group, through='UserGroup')
    totp_phrase = models.CharField(max_length=255, default='')
    is_admin = models.BooleanField(default=False)
    is_super = models.BooleanField(default=False)