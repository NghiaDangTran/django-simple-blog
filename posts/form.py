
from logging import PlaceHolder
from django import forms
from django.forms import ModelForm
from .models import Post

class PostForm(ModelForm):
    class Meta:
        model= Post
        fields=("title","body")
        labels={
            'title':''
            ,'body':''

        }
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'Post title'},)
            ,'body':forms.TextInput(attrs={'class':'form-control','placeholder':'Post body'})
        }