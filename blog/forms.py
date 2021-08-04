from django import forms
from .models import blogpost , ProfileModel


class Myblogform(forms.ModelForm):
    choices=(('','Select Topic'),('Educational','Educational'),('Informational','Informational'),('Funny Thoughts/Jokes','Funny Thoughts/Jokes'),
    ('About Me','About Me'),('Sayri','Sayri'),('Other','Other'))
    topic=forms.ChoiceField(choices=choices,widget=forms.Select(attrs={'class':'form-control'}),required=True)
    
    
    class Meta:
        model=blogpost
        fields=['topic','title','post']
        widgets={'title':forms.TextInput(attrs={'class':'form-control'}),'post':forms.Textarea(attrs={'class':'form-control'})}


class ProfileForm(forms.ModelForm):
    class Meta:
        model=ProfileModel
        fields=['full_name','profile_picture', 'bio', 'facebook_url', 'instagram_url']
        widgets={'full_name':forms.TextInput(attrs={'class':'form-control'}),'bio':forms.Textarea(attrs={'class':'form-control'}),'facebook_url':forms.TextInput(attrs={'class':'form-control'}),'instagram_url':forms.TextInput(attrs={'class':'form-control'})}
