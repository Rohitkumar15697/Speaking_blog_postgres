from django.contrib.auth.models import User
from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import blogpost,ProfileModel
from django.views.generic import DeleteView
from django.shortcuts import get_object_or_404
from .forms import Myblogform, ProfileForm

import random
# Create your views here.

@login_required(login_url='login')
def profile(request):
    count=0

    postdata=blogpost.objects.all().filter(created_by=request.user)
    #print(list(postdata))
    
    count=len(postdata)
    
    fulldata=postdata[:2]  #Printing only current blog on the profile

    postdata=postdata[:8]  #Pring total 15 blogs title from first blog

    #Accessing profile detail from ProfileModel of user
    
    profile_detail=ProfileModel.objects.all().filter(profile_name=request.user)

    return render(request,'profile.html' ,{'data':postdata,'fulldata':fulldata,'count':count,"profile_detail":profile_detail})



@login_required(login_url='login')
def add_blog(request):
    fm=Myblogform()
    if request.method=='POST':
        fm=Myblogform(request.POST)
        if fm.is_valid():
            topic=fm.cleaned_data['topic']
            title=fm.cleaned_data['title']
            post=fm.cleaned_data['post']
            obj=blogpost(topic=topic,title=title,post=post)
    
            obj.created_by=request.user  #this line fill the created_by column in models by current username automatically
            obj.save()
            return redirect('profile')
    return render(request, 'add_blog.html',{'form':fm})

@login_required(login_url='login')
def confirm_logout(request):
    return render(request, 'confirm_logout.html')

@login_required(login_url='login')
def logoutme(request):
    logout(request)
    return redirect('/')

class DeleteAccount(DeleteView):
    model=User
    template_name='confirm_delete_account.html'
    success_url= reverse_lazy('home')


#Add user profile detail
@login_required(login_url='login')
def add_profile_detail(request):
    form=ProfileForm()
    if request.method=="POST":
        form=ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            full_name=form.cleaned_data['full_name']
            profile_picture=form.cleaned_data['profile_picture']
            bio=form.cleaned_data['bio']
            facebook_url=form.cleaned_data['facebook_url']
            instagram_url=form.cleaned_data['instagram_url']
            obj=ProfileModel(full_name=full_name, profile_picture=profile_picture, bio=bio, facebook_url=facebook_url,instagram_url=instagram_url)
            obj.profile_name=request.user
            obj.save()
            return redirect('profile')
    return render(request, 'add_profile_detail.html',{'form':form})


#View for showing any user data
def Show_User_Data(request,username):
    user=get_object_or_404(User, username=username)
    if ProfileModel.objects.all().filter(profile_name=user):
        data=get_object_or_404(ProfileModel,profile_name=user.id)
        bloglinks=blogpost.objects.all().filter(created_by=user.id)
        args={'user':user,'data':data,'bloglinks':bloglinks}
        return render(request, 'profile_detail.html',args)
    else:
        return HttpResponse(f'{user.username} Not updated Profile yet!')
