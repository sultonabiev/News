from django import forms
from django.forms import ModelForm, TextInput, Textarea, FileInput
from .models import Task, MyImage

class ArticleForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title", "task", "category", "image"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название'
            }),
            "task": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите саму статью'
            }),
            "category": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите категорию'
            }),
            "image": FileInput(attrs={'class': 'form-control'}),
        }

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = MyImage
        fields = ['name', 'image']
