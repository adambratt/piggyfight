from twilio.twiml import Response
from django_twilio.decorators import twilio_view
from django.views.decorators.http import require_POST
from django.http import HttpResponse
from game.models import Post
import logging

log = logging.getLogger(__name__)


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

#@require_POST
def mailgun(request):
    sender    = request.POST.get('sender')
    subject   = request.POST.get('subject', '')
    body = request.POST.get('body-plain', '')
    log.debug("got post")

    # attachments:
    for key in request.FILES:
        file = request.FILES[key]
        log.debug("got files")
        form=PhotoForm(request.POST, { key: file })
        log.debug("got form")
        if form.is_valid():
            log.debug("got valid form")
            newphoto=form.save()
            newphoto.member = request.user.get_profile()
            post=Post(newphoto)
            post.member = request.user.get_profile()
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

def handle_upload(file):
    destination = open('some/file/name.txt', 'wb+')
    for chunk in f.chunks():
        destination.write(chunk)
    destination.close()