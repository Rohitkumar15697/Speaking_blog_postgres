from django.contrib.auth.models import User
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


#View for showing any user data
def Show_User_Data(request,username):
    user=User.objects.get(username=username)
    data=ProfileModel.objects.get(profile_name=user.id)
    bloglinks=blogpost.objects.all().filter(created_by=user.id)
    args={'data':data,'bloglinks':bloglinks}
    return render(request, 'profile_detail.html',args)