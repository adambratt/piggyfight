from twilio.twiml import Response
from django_twilio.decorators import twilio_view
from django.views.decorators.http import require_POST
from django.http import HttpResponse
from game.models import Post, Activity
from django.contrib.csrf.middleware import csrf_exempt
from django.conf import settings
from django.contrib.auth.models import User
from django.utils import simplejson
import logging
from django.shortcuts import render, redirect
from images.models import photo_upload_name, Photo

log = logging.getLogger(__name__)


def loader(request):
    if request.POST.get("last"):
        obj = Activity.objects.filter(pk__gt=request.POST.get("last"))
    else:
        obj = Activity.objects.order_by('pk')
    if not obj or obj.count() < 1:
        return HttpResponse("{}")
    obj = obj[0]
    data = {}
    data['id'] = obj.pk
    data['img'] = obj.img
    data['user'] = obj.user.username
    data['log'] = obj.log
    data['time'] = "Just Now"
    return HttpResponse(simplejson.dumps(data))

def home(request):
    return redirect('/members/login/')

def rules(request):
    return

def leaderboard(request):
    return

def verify(request):
    return

def group(request, group_id):
    return

def join_group(request, group_id):
    return

def create_group(request):
    return

@csrf_exempt
#@require_POST
def mailgun(request):
    sender    = request.POST.get('sender')
    subject   = request.POST.get('subject', '')
    body = request.POST.get('body-plain', '')

    # attachments:
    for key in request.FILES:
        file = request.FILES[key]
        filename = handle_upload(file)
        log.debug("got files")
        post=Post(photo=filename+".jpg")
        post.save()
        use=User.objects.get(pk=2)
        log = Activity(img='/common/'+filename+'.jpg', user=use, log='Just uploaded a receipt (Pending Verification)', time='Just Now')
        log.save();
    
    log.debug("done")
    # Returned text is ignored but HTTP status code matters:
    return HttpResponse('OK')

@twilio_view
def twilio(request):
    r = Response()
    r.sms('Your message has been received and will be verified shortly!')
    return r


#### Functions ####

def handle_upload(f):
    name = photo_upload_name(True, "blah")
    destination = open(settings.MEDIA_ROOT+"/"+name+".jpg", 'wb+')
    for chunk in f.chunks():
        destination.write(chunk)
    destination.close()
    return name