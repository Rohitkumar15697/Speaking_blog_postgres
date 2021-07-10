from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import widgets

class createuser(UserCreationForm):
    password1=forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class':'form-control','style':'width:400px;'}))
    password2=forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class':'form-control','style':'width:400px;'}))
    email=forms.EmailField(required=True, widget=forms.TextInput(attrs={'class':'form-control','style':'width:400px;'}))
    #first_name=forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control','style':'width:400px;'}))
    #last_name=forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control','style':'width:400px;'}))
    class Meta:
        model=User
        fields=['username','password1','password2','email']
        widgets={'username':forms.TextInput(attrs={'class':'form-control','style':'width:400px;'})}

class loginform(forms.Form):
    username=forms.CharField(max_length=122,required=True,widget=forms.TextInput(attrs={'class':'form-control','style':'width:400px;'}))
    password=forms.CharField(max_length=122,widget=forms.PasswordInput(attrs={'class':'form-control','style':'width:400px;'}),required=True,)