from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import UserProfile
import re

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="Password")
    password2 = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    country = forms.CharField(required=True)
    city = forms.CharField(required=True)
    photo = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean_password2(self):
        p1 = self.cleaned_data.get('password')
        p2 = self.cleaned_data.get('password2')
        if p1 != p2:
            raise ValidationError("Passwords do not match.")

        # Ek regex kontrolü: en az 8 karakter, 1 rakam, 1 özel karakter
        pattern = r'^(?=.*[0-9])(?=.*[^a-zA-Z0-9]).{8,}$'
        if not re.match(pattern, p1):
            raise ValidationError("Password must be >=8 chars, 1 digit & 1 special char.")
        return p2

class SearchForm(forms.Form):
    office = forms.CharField(required=False, label="Office Name")
    date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type':'date'}))
    time = forms.TimeField(required=False, widget=forms.TimeInput(attrs={'type':'time'}))
