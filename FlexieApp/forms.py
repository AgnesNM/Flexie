from django import forms

class UserInput(forms.ModelForm):
    class Meta:
        model = FlexieUsers
        fields = ('email', 'username', 'file')
        widgets = {
            'password': forms.PasswordInput(),
        }

