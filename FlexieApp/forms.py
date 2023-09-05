from django import forms

# class UserInput(forms.Form):
#     username = forms.CharField()
#     email = forms.EmailField() 
#     password = forms.CharField(widget=forms.PasswordInput)



class UserInput(forms.Form):
    username = forms.CharField(
        label = "username",
        max_length = 80,
        required = True,
    )

    email = forms.EmailField(
        label = "email",
        max_length = 80,
        required = True,
    )

    password = forms.CharField(
        widget=forms.PasswordInput,
        label = "password",
        max_length = 80,
        required = True,
    )

    