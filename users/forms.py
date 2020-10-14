from django import forms

class SignUpForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())