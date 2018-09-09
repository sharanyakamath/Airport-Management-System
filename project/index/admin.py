from django.contrib import admin

# Register your models here.
from .models import Users
from .models import Flight
from .models import Security
from .models import Staff

admin.site.register(Users)
admin.site.register(Flight)
admin.site.register(Security)
admin.site.register(Staff)
