from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime
import django.utils.timezone
# Create your models here.


class Flight(models.Model):
    flight_no = models.IntegerField(primary_key=True, default=1007)
    airline_name = models.CharField(max_length=50)
    no_of_seats = models.IntegerField(default=0)
    source = models.CharField(max_length=50)
    source_code = models.CharField(max_length=3)
    destination = models.CharField(max_length=50)
    destination_code = models.CharField(max_length=3)
    arrival_time = models.DateTimeField()
    departure_time = models.DateTimeField()


class Passenger(models.Model):
    pnr = models.CharField(max_length=10)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dob = models.DateField(default=1/1/1990)
    nationality = models.CharField(max_length=50)
    gender = models.CharField(max_length=1)
    flight_no = models.ForeignKey(Flight, on_delete=models.CASCADE, default=1007)
    checked_in_status = models.BooleanField(default=0)
    cleared_security_status = models.IntegerField(default=0)


class User(AbstractUser):
    USER_TYPE_CHOICES = (
      (1, 'flightstaff'),
      (2, 'security'),
      (3, 'admin'),
    )

    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, default=3)


class Security(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=2)
    id = models.IntegerField(primary_key=True)


class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=1)
    id = models.IntegerField(primary_key=True)
    flight_no = models.ForeignKey(Flight, on_delete=models.CASCADE, default=1007)
