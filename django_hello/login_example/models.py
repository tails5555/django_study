from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver

class Job(models.Model) :
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, default="Job Name")

class Account(models.Model) :
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=100, default='City Address')
    birthday = models.DateField(default=timezone.now())
    job = models.ForeignKey(Job, on_delete=models.CASCADE, default=None)