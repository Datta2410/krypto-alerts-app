from django.db import models

# Create your models here.


class Users(models.Model):
    UserId = models.AutoField(primary_key=True)
    UserName = models.CharField(max_length=500)
    Password = models.CharField(max_length=500)
    JWT = models.CharField(max_length=500)

class Alerts(models.Model):
    AlertId = models.AutoField(primary_key=True)
    AlertStatus = models.CharField(max_length=500)