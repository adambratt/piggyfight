from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=255)
    
class Store(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey('game.Category', blank=True)
    
class Post(models.Model):
    mainphoto=models.ForeignKey('images.Photo',related_name="post_mainphoto",null=True,blank=True,on_delete=models.SET_NULL)
    store = models.ForeignKey('game.Store')
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    savings = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    percent = models.IntegerField()
    verified = models.BooleanField(default=False)

class Activity(models.Model):
    feed = models.ForeignKey(User, related_name="activity_feed")
    user = models.ForeignKey(User, related_name="activity_user")
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