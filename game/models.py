from django.db import models
from django.contrib.auth.models import User


#### Functions ####

def upload_name(instance, filename):
    randomname = hashlib.md5(str(random.randint(0,1000000))).hexdigest()
    fullname = os.path.join("images/full/",randomname)
    try:
        Photo.objects.get(photo=fullname)
        return photo_upload_name(instance,filename)
    except Photo.DoesNotExist:
        return fullname

#### Models ####

class Category(models.Model):
    name = models.CharField(max_length=255)
    
class Store(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey('game.Category', blank=True)
    
class Post(models.Model):
    member = models.ForeignKey('members.Member')
    photo=models.ForeignKey('images.Photo',related_name="post_mainphoto",null=True,blank=True,on_delete=models.SET_NULL)
    store = models.ForeignKey('game.Store', blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    savings = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    percent = models.IntegerField(default=0)
    verified = models.BooleanField(default=False)
    create_ts=models.DateTimeField(auto_now_add=True)
    
class Verify(models.Model):
    post = models.ForeignKey(Post)
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    savings = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    count = models.IntegerField(default=0)
    
class MMS(models.Model):
    sender = models.CharField(max_length=50)
    body = models.TextField(blank=True)
    photo = models.ImageField(upload_to=upload_name, blank=True)

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
    owner = models.ForeignKey('members.Member', related_name='group_owner')
    members=models.ManyToManyField('members.Member', related_name='group_people', through='members.Membership',blank=True)