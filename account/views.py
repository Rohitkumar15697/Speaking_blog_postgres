from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .form import createuser,loginform
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def register(request):
    if request.method=='POST':
        fm=createuser(request.POST)
        useremail=request.POST['email']
        username=request.POST['username']
        print(useremail)

        #Sending Thank you E-mail
        email_subject="From SpeakingBlog"
        email_message=f"Thank you {username} for creating account in 'www.speaksera.co.in'. Now go to login (https://speakingblog.herokuapp.com/account/login/) and enjoy your with your account. "                
        email_from=settings.EMAIL_HOST_USER
        email_to=[useremail,'rohitkumar.kumar15697@gmail.com']
        send_mail(email_subject,email_message,email_from,email_to, fail_silently=False)

        if fm.is_valid():
            fm.save()
            messages.success(request,'Account is created successfully!')
            return redirect('register')
    else:
        fm=createuser()
    return render(request,'account.html',{'form':fm})




def loginme(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            print('Your are logged in')
            return redirect('/blog/profile/')
        else:
            messages.error(request,'Incorrect username or password!')

    fm=loginform()
    return render(request,'login.html',{'form':fm})