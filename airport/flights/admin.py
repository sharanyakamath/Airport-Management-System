from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.
from .models import Users, Flight, Security, Staff
from .forms import UsersCreationForm, UsersChangeForm

class UsersAdmin(UserAdmin):
    add_form = UsersCreationForm
    form = UsersChangeForm
    list_display =['pnr', 'username', 'email', 'first_name', 'last_name', 'dob', 'nationality', 'gender', 'flight_no', 'checked_in_status', 'cleared_security_status']
    model = Users

admin.site.register(Users, UsersAdmin)
admin.site.register(Flight)
admin.site.register(Security)
admin.site.register(Staff)
