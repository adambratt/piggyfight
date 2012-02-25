from django.db import models
import hashlib
import random
import os


# Utility Functions
def photo_upload_name(instance, filename):
    randomname = hashlib.md5(str(random.randint(0,1000000))).hexdigest()
    fullname = os.path.join("images/full/",randomname)
    try:
        Photo.objects.get(photo=fullname)
        return photo_upload_name(instance,filename)
    except Photo.DoesNotExist:
        return fullname

# Create your models here.
class Album(models.Model):
    name=models.CharField(max_length=128)

class Photo(models.Model):
    name=models.CharField(max_length=100,blank=True,unique=True)
    photo=models.ImageField(upload_to=photo_upload_name,blank=False)
    album=models.ForeignKey(Album,null=True,blank=True)
    member=models.ForeignKey("members.Member")
    caption=models.TextField(blank=True, null=True)
    create_ts=models.DateTimeField(auto_now_add=True)
    def save(self, *args, **kwargs):
        super(Photo, self).save(*args, **kwargs) 
        if len(self.name)==0:
            self.name=os.path.basename(self.photo.name)
        super(Photo, self).save(*args, **kwargs) 
    
    