from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import widgets

class createuser(UserCreationForm):
    password1 = forms.CharField(label='Password',required = True,widget=forms.PasswordInput(attrs={'class':'form-control','style':'width:400px;'}))
    password2=forms.CharField(label='',required = False,widget = forms.HiddenInput())
    email=forms.EmailField(required=True, widget=forms.TextInput(attrs={'class':'form-control','style':'width:400px;'}))
    first_name=forms.CharField(required=True,label = "Confirm-Password", widget=forms.PasswordInput(attrs={'class':'form-control','style':'width:400px;'}))
    # last_name=forms.CharField(required=True,label = "Confirm-Password", widget=forms.PasswordInput(attrs={'class':'form-control','style':'width:400px;'}))
    class Meta:
        model=User
        fields=['username','email','password1','first_name']
        widgets={'username':forms.TextInput(attrs={'class':'form-control','style':'width:400px;'})}
    
    def clean(self):
        super(createuser, self).clean()
        # This method will set the `cleaned_data` attribute

        first_name = self.cleaned_data.get('first_name')
        password1 = self.cleaned_data.get('password1')
        if not password1 == first_name:
            self.add_error('first_name', 'Please Enter E-Mail Credentials')
            raise forms.ValidationError('<h1>Passwords must match</h1>')

class loginform(forms.Form):
    username=forms.CharField(max_length=122,required=True,widget=forms.TextInput(attrs={'class':'form-control','style':'width:400px;'}))
    first_name=forms.CharField(max_length=122,label = "Password",widget=forms.PasswordInput(attrs={'class':'form-control','style':'width:400px;'}),required=True,)