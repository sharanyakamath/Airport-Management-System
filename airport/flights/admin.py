from django.contrib import admin

# Register your models here.
from .models import User, Passenger, Flight, Security, Staff

admin.site.register(User)
admin.site.register(Passenger)
admin.site.register(Flight)
admin.site.register(Security)
admin.site.register(Staff)