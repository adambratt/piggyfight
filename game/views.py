from twilio.twiml import Response
from django_twilio.decorators import twilio_view
from django.views.decorators.http import require_POST
from django.http import HttpResponse
from game.models import Post
from django.contrib.csrf.middleware import csrf_exempt
from django.conf import settings
import logging
from django.shortcuts import render, redirect
from images.models import photo_upload_name, Photo

log = logging.getLogger(__name__)


def loader(request):
    return

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