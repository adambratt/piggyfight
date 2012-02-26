from PIL import Image
from django.shortcuts import redirect
from images.models import Photo
from django.http import Http404 

import settings
import os

# Create your views here.
def load(request, image_id, **kwargs):
    try:
        p = Photo.objects.get(name=image_id)
    except:
        raise Http404
    
    if (not 'width' in kwargs) or (not 'height' in kwargs):
        size = 'full'
    else:
        size = kwargs['width']+'x'+kwargs['height']
    
    # get size dir/check if image exists
    sizedir=settings.MEDIA_ROOT+'images/'+size+'/'
    
    if os.path.isfile(sizedir+image_id):
        return redirect(settings.MEDIA_URL+'images/'+size+'/'+image_id)
    elif size == 'full':
        return Http404 # Must not exist
    
    # make image dir
    if not os.path.exists(sizedir):
        os.makedirs(sizedir)
        
    # open up the image
    img=Image.open(p.photo.path)
    if img.mode not in ('L','RGB'):
            img=img.convert('RGB')
    img=img.resize((int(kwargs['width']), int(kwargs['height'])), Image.ANTIALIAS)
    img.save(sizedir+image_id,'PNG')
    
    return redirect(settings.MEDIA_URL+'images/'+size+'/'+image_id)