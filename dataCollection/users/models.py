from django.db import models
from django.conf import settings

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from datetime import timedelta
from django.utils.timezone import now

'''
class TurfPlayer(AbstractUser):
    is_verified = models.BooleanField(default=False)

class EmailOTP(models.Model):
    email = models.EmailField(max_length=254)
    otp = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    is_verified = models.BooleanField(default=False)

    def is_expired(self):
        return now() > self.created_at + timedelta(minutes=5)  # OTP valid for 5 min
'''    
class ExtraInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="extraInfo")
    phone_no = models.IntegerField(max_length=10)
    address = models.TextField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.phone_no
