from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class Member(models.Model):
    user=models.OneToOneField(User, primary_key=True) 
    total_points=models.IntegerField(default=25)
    mainphoto=models.ForeignKey('images.Photo',related_name="members_mainphoto",null=True,blank=True,on_delete=models.SET_NULL)
    def __unicode__(self):
        return self.user.username
    def _get_avatar(self):
        if(self.mainphoto): 
            return '/image/'+self.mainphoto.name+'/avatar/'
        return settings.STATIC_URL+'images/avatar.png' 
    def _get_thumb(self):
        if(self.mainphoto):
            return '/image/'+self.mainphoto.name+'/thumb/'
        return settings.STATIC_URL+'images/thumb.png'
    thumb=property(_get_thumb)
    avatar=property(_get_avatar)


#Signal for creating member profile on user creation
def add_member(sender, instance, created, **kwargs):
    if created:
        member=Member.objects.create(user=instance)
        
post_save.connect(add_member, sender=User)

class Membership(models.Model):
    member=models.ForeignKey('Member')
    group=models.ForeignKey('game.Group')
    create_ts=models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return self.member.user.username+' in '+self.group.name