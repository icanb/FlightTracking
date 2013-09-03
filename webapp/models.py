

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from import_export import resources as export


class Flight(models.Model):
    flight_number = models.TextField(blank=True)
    date = models.DateTimeField(null=True, blank=True)
    from_val = models.TextField(blank=True)
    destination = models.TextField(blank=True)
    capacity = models.FloatField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    flyer = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='flights', null=True, blank=True)


class House(models.Model):
    address = models.TextField(blank=True)
    size = models.FloatField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)


class User(AbstractUser):
    pass


class FlightDataResource(export.ModelResource):

    class Meta:
        model = Flight


class HouseDataResource(export.ModelResource):

    class Meta:
        model = House


class UserDataResource(export.ModelResource):

    class Meta:
        model = User
