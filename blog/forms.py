
from .models import  Post, UserProfile, Comment
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class CreatePost(forms.ModelForm):
    class Meta():
        model = Post
        fields = '__all__'
        exclude = ('author','likes')
        # widget = {
        #     'author' : forms.Select(attrs= {'disabled' : 'disabled'})
        # }

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields["author"].disabled = True
    #     # Or to set READONLY

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'message')

        # widgets = {
        #     'name' : forms.TextInput(attrs= {'class' : 'form-group'}),
        #     'message' : forms.Textarea(attrs= {'class' : 'form-group'}),
        # }