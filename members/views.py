from django.shortcuts import render, redirect
from members.forms import PhotoForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from members.forms import RegistrationForm
from django.contrib.auth.models import User

##### Views #####

@login_required
def dashboard(request):
    feed = build_feed(request.user.get_profile())
    return render(request, 'members/dashboard.html', {})

@login_required
def logout(request):
    django.contrib.auth.logout(request)
    return redirect('/')

def register(request):
    if request.user.is_authenticated():
        return redirect('/dashboard/')
    if request.method=='POST':
        form=RegistrationForm(request.POST)
        if form.is_valid():
            # Generate a username and create user
            new_user=User.objects.create_user(form.cleaned_data['username'], form.cleaned_data['email'], form.cleaned_data['password1'])
            new_user.save()
            log_user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
            login(request, log_user)
            return redirect('/dashboard/')
    else:
        form=RegistrationForm()
    return render(request,'members/register.html',{'form':form})


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
    return display(request,'members/upload_photo.html',{'form':form, })


##### Functions #####

def build_feed(profile):
    return

def display(request, template, dict={}):
    dict['profile']=request.user.get_profile()
    return render(request, template, dict)