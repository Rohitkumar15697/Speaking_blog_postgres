from django import forms
from .models import blogpost 


class Myblogform(forms.ModelForm):
    choices=(('None','Select Your Topic'),('Educational','Educational'),('Informational','Informational'),('Funny Thoughts/Jokes','Funny Thoughts/Jokes'),
    ('About Me','About Me'),('Sayri','Sayri'))
    topic=forms.ChoiceField(choices=choices,widget=forms.Select(attrs={'class':'form-control'}))
    class Meta:
        model=blogpost
        fields=['topic','title','post']
        widgets={'title':forms.TextInput(attrs={'class':'form-control'}),'post':forms.Textarea(attrs={'class':'form-control'})}


