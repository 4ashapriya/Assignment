from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=20, null=True, blank=True)
    age = models.CharField(max_length=2, null=True, blank=True)
    addrs = models.CharField(max_length=30, null=True, blank=True)
    hobbies = models.CharField(max_length=20, null=True, blank=True)
    fav_movies = models.CharField(max_length=20, null=True, blank=True)

