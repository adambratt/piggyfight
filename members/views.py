


##### Views #####

def dashboard(request):
    feed = build_feed(request.user.get_profile())
    return

def login(request):
    return

def register(request):
    return

@login_required    
def upload_photo(request):
    profile=request.user.get_profile()
    if request.method=='POST':
        form=PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            newphoto=form.save(commit=False)
            newphoto.member=profile
            newphoto.save()
            profile.mainphoto=newphoto
            profile.save()
            return redirect('/dashboard/')
    else:
        form=PhotoForm()
    return render(request,'members/upload_photo.html',{'form':form, 'profile': profile})

##### Functions #####

def build_feed(profile):
    return