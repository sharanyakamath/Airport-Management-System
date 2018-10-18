from django.db import models
from django.contrib.auth.models import AbstractUser
import django.utils.timezone
# Create your models here.
class Flight(models.Model):
    flight_no = models.IntegerField(primary_key=True,default=1007)
    airline_name = models.CharField(max_length=50)
    no_of_seats = models.IntegerField(default=0)
    source = models.CharField(max_length=50)
    destination = models.CharField(max_length=50)
    arrival_time = models.DateTimeField()
    departure_time = models.DateTimeField()

class Users(AbstractUser):
    pnr = models.CharField(max_length=10, primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dob = models.DateField(default=1/1/1990)
    nationality = models.CharField(max_length=50)
    gender = models.CharField(max_length=1)
    flight_no = models.ForeignKey(Flight, on_delete=models.CASCADE, default=1007)
    checked_in_status = models.BooleanField(default=0)
    cleared_security_status = models.IntegerField(default=0)

class Security(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name =  models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

class Staff(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name =  models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    flight_no = models.ForeignKey(Flight, on_delete=models.CASCADE, default=1007)
