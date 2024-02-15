from django import forms 

class Loginform(forms.Form):
    # Login form for the user containing username and password
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
