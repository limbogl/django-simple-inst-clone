from django.forms import ModelForm
from .models import *


class CreatePostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        exclude = ['profile', 'date_created']


class UpdatePostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['post_title']

