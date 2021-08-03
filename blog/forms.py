from django import forms
from django.forms.fields import EmailField
from .models import Author, Blog

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'
        labels = {
            "author": "Name Of Author",
            "bio": "Author's Bio"
        }

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'
        labels = {
            "title": "Blog's Title",
            "description": "Blog's Description",
            "author": "Blog's Author"
        }

    def __init__(self, *args, **kwargs):
        super(BlogForm, self).__init__(*args, **kwargs)
        self.fields['author'].empty_label = "Select"