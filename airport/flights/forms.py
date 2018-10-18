from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Users
class UsersCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Users
        fields = ('pnr', 'username', 'first_name', 'last_name', 'email', 'dob', 'nationality', 'gender', 'flight_no', )
class UsersChangeForm(UserChangeForm):
    class Meta:
        model = Users
        fields = ('pnr', 'username', 'first_name', 'last_name', 'email', 'dob', 'nationality', 'gender', 'flight_no', )
