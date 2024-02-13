from django import forms
from .models import messages
from django.forms.widgets import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class Userreg(UserCreationForm):
    username = forms.CharField(max_length=20,required=False,widget=TextInput)
    password1 = forms.CharField(max_length=15,min_length=5,required=False,widget=PasswordInput)
    password2 = forms.CharField(min_length=5,max_length=15,widget=PasswordInput,required=False)
    class Meta:
        model = User
        fields = ['username',
                  'password1',
                  'password2',
        ]
class Msgform(forms.ModelForm):
    text = forms.CharField(widget=TextInput)
    class Meta:
        model = messages
        fields = ('text',)








