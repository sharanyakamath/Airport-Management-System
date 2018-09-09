from django.db import models

# Create your models here.
class Flight(models.Model):
    flight_no = models.IntegerField(primary_key=True)
    airline_name = models.CharField(max_length=50, default='john doe')
    no_of_seats = models.IntegerField(default=0)
    source = models.CharField(max_length=50, default='Delhi')
    destination = models.CharField(max_length=50, default='Mumbai')
    arrival_time = models.DateTimeField()
    departure_time = models.DateTimeField()

class Users(models.Model):
    pnr = models.CharField(max_length=10, primary_key=True)
    first_name = models.CharField(max_length=50, default='john')
    last_name = models.CharField(max_length=50, default='doe')
    dob = models.DateField(default=1/1/1990)
    nationality = models.CharField(max_length=50, default='India')
    gender = models.CharField(max_length=1, default='M')
    flight_no = models.ForeignKey(Flight, on_delete=models.CASCADE)
    checked_in_status = models.BooleanField(default=0)
    cleared_security_status = models.IntegerField(default=0)

class Security(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name =  models.CharField(max_length=50, default='john')
    last_name = models.CharField(max_length=50, default='doe')
    password = models.CharField(max_length=50)

class Staff(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name =  models.CharField(max_length=50, default='john')
    last_name = models.CharField(max_length=50, default='doe')
    password = models.CharField(max_length=50)
    flight_no = models.ForeignKey(Flight, on_delete=models.CASCADE)
