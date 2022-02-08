from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
# Create your models here.

class Chat(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    comment=models.CharField(max_length=1000)
    date=models.DateField()

admin.site.register(Chat)