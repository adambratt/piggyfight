from django.db import models
from django.contrib.auth.models import User


class Category(models.model):
    name = models.CharField(max_lenth=255)

class Activity(models.Model):
    feed = models.ForeignKey(User)
    user = models.ForeignKey(User)
    log = models.CharField(max_length=255)
    create_ts=models.DateTimeField(auto_now_add=True)
    
class Badge(models.Model):
    name = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    
class Group(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    owner = models.ForeignKey('members.Member')
    members=models.ManyToManyField('members.Member', through='members.Membership',blank=True)