from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('manager', 'Manager'),
        ('reader', 'Reader'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='reader')
    phone = models.CharField(max_length=9)

class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='profile')
    birth_date = models.DateField(blank=True, null=True)
    avatar = models.ImageField(upload_to='profile_img', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)