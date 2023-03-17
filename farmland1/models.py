from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User


class Registration(models.Model):
    First_name = models.CharField(max_length=200, null = True)
    Last_name = models.CharField(max_length=200, null = True)
    Email = models.EmailField(max_length=200, null = True)
    Password = models.CharField(max_length=200, null = True)
    Registration_date = models.DateField(null = True)
    Image = models.ImageField(upload_to='media', null = True)
    About_website = models.TextField(null = True)
    User_role = models.CharField(max_length=200, null = True)
    user = models.OneToOneField(User,on_delete = models.CASCADE, null = True)

    def __str__(self):
        return self.First_name


class Schedule_worker(models.Model):
    work = models.CharField(max_length=200, null = True)
    work_reg =  models.ForeignKey(Registration,on_delete = models.CASCADE, null = True)