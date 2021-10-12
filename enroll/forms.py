from django import forms
from django.db.models import fields
from django.forms import widgets
from . import models

class StuderntRegistration(forms.ModelForm):
    class Meta:
        model = models.User
        fields = ['name', 'email', 'password']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control','id':'nameid'}),
            'email': forms.EmailInput(attrs={'class':'form-control','id':'emailid'}),
            'password': forms.PasswordInput(attrs={'class':'form-control','id':'passwordid'})
        }