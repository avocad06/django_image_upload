from dataclasses import fields
from pyexpat import model
from socket import fromshare
from django import forms
from .models import Article

class CreateForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'content', 'image')