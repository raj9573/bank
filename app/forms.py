from django import forms 
from app.models import *
from django.core import validators
class User_Form(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','email','password']
        widgets={'password':forms.PasswordInput}




class Profile_form(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['aadhar_number','address','profile_pic']
        