from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.core import validators


class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    aadhar_number=models.IntegerField(primary_key=True)
    address=models.TextField()
    profile_pic=models.ImageField()

    