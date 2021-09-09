from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import widgets

class registerform(UserCreationForm):
    class Meta:
        model = User
        fields =['username','email','password1','password2']
    def __init__(self, *args, **kwargs):
        super(registerform, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Name'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'

