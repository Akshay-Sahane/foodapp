from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import MyUser

class UserForm(UserCreationForm):
    class Meta:
        model=MyUser
        fields=('first_Name','last_Name','mobile_Number','password1','password2','user_Role','address')
        widgets={
            'password1':forms.CharField(help_text="hii"),
            'password2':forms.CharField(help_text="hii"),
            'user_Role':forms.HiddenInput(attrs={'value':'customer','m':'1'}),
            'address':forms.Textarea(attrs={'rows':'5','cols':'30','m':'1'}),
               }

class AdminForm(UserCreationForm):
    class Meta:
        model=MyUser
        fields=('first_Name','last_Name','mobile_Number','password1','password2','user_Role','address')
        widgets={
            'password1':forms.CharField(help_text="hii"),
            'password2':forms.CharField(help_text="hii"),
            'user_Role':forms.HiddenInput(attrs={'value':'customer','m':'1'}),
            'address':forms.Textarea(attrs={'rows':'5','cols':'30','m':'1'}),
        }

