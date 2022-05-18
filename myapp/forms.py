from tkinter import Widget
from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField,UserChangeForm
from django.contrib.auth.models import User
from django.shortcuts import redirect
from .models import *
from django.contrib.auth import get_user_model



class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username','first_name','email','roles']
        Widget = {
            'role': forms.Select(attrs={'class':'form-control'}),
            'first_name': forms.TextInput(attrs={'class':'form-control'}),
            'username': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.TextInput(attrs={'class':'form-control'}),
            'password': forms.PasswordInput(),

        }

class  LoginForm(AuthenticationForm):
    username=forms.CharField(label='Username')
    password=forms.CharField(label='password',widget=forms.PasswordInput(),help_text='1. Must Have A Special Character')
    
class EditProfile(UserChangeForm):
    class Meta:
        model=User
        fields=['first_name','speciality','clinic_name','gender','address']

        Widget={
            'first_name': forms.TextInput(attrs={'class':'form-control'}),
            'clinic_name': forms.TextInput(attrs={'class':'form-control'}),
            'password': forms.PasswordInput(),
            'address': forms.TextInput(attrs={'class':'form-control'}),

        }
#<<<<< patienc edit >>>>>>#
class EditProfile1(UserChangeForm):
    class Meta:
        model=User
        fields=['first_name','gender','address']

    Widget={
            'first_name': forms.TextInput(attrs={'class':'form-control'}),
            'address': forms.TextInput(attrs={'class':'form-control'}),
            'gender': forms.TextInput(attrs={'class':'form-control'}),



          

    }
    #<<<<< Doctor Slot Add >>>>>>#
class SlotForm(forms.ModelForm):
     class Meta:
        model=Slot
        fields=['weeks','timeslot'] 
        
        widgets = {
            'weeks': forms.Select(attrs={'class':'form-control'}),
            'timeslot': forms.Select(attrs={'class':'form-control'}),
            
        }
class Slotupdate(forms.ModelForm):
    class Meta:
        model=Slot
        fields=['weeks','timeslot'] 
        
        widgets = {
            'weeks': forms.Select(attrs={'class':'form-control'}),
            'timeslot': forms.Select(attrs={'class':'form-control'}),
        }

#<<<<<<<<<<<<< Patience Profile >>>>>>>>>>>>>>>#
class Profile(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','gender','address','profile']
        label = {'first_name':'Name','gender':'Gender','address':'Address','profile':'Profile'}
        error_messages = {'name':{'required':'Enter Your Name'},
        'password':{'required':'Enter Your Password'},
        'address' :{'required':'Enter Your Address'},
        
        }

    Widget={
            'first_name': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your Name'}),
            'address': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Address Here'}),
            'gender': forms.TextInput(attrs={'class':'form-control'}),
            #'profile': forms.ImageField(attrs={'class':'form-control'}),

    }


