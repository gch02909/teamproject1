# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class PCRoom(models.Model):
    name = models.CharField(max_length=50)
    cost = models.IntegerField()
    spec = models.TextField()
    maxPeopleNumber = models.IntegerField()
    peopleNumber = models.IntegerField()
    misc = models.CharField(max_length=50)

class Seat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pcroom = models.ForeignKey(PCRoom, on_delete=models.CASCADE)
    accupied = models.BooleanField(default=False)
    
class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    representName = models.CharField(max_length=20)
    groupName = models.CharField(max_length=50)
    pcroom = models.ForeignKey(PCRoom, on_delete=models.CASCADE)
    peopleNumber = models.IntegerField()
    representContact = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    startDate = models.DateTimeField(default=now)
    endDate = models.DateTimeField(default=now)
    sponsor = models.CharField(max_length=20, default='없음')