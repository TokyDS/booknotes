from django import forms
from api.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class BookAdd(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'author', 'cover', 'book')
        
        
class ConspectAdd(forms.ModelForm):
    class Meta:
        model = Conspect
        fields = ( 'book', 'text',)
        
class NoteAdd(forms.ModelForm):
    class Meta:
        model = Note
        fields = ( 'book', 'text',)
        
class LoginForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']