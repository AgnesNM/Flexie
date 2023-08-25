from django import forms

class UserInput(forms.Form):
    username = forms.CharField()
    email = forms.EmailField() 
    password = forms.CharField(widget=forms.PasswordInput)
    