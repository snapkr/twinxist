from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(required=True, max_length=30)
    password = forms.CharField(required=True, widget=forms.PasswordInput(), max_length=128)
