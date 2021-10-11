from django import forms
from django.forms import fields, widgets
from .models import Post

class UploadForm(forms.ModelForm):

    class Meta:
        model =Post
        fields = ['title', 'image_caption', 'image']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'title'}),
            'image_caption': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'image-caption'}),
            'image': forms.FileInput(attrs={'class':'mt-3  border-0'}),
        }