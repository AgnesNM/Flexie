from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import FlexieUsers


class UserInput(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-detectFraud'
        self.helper.form_class = 'detectForms'
        self.helper.form_method = 'post'
        self.helper.form_action = 'detect fraud'

        self.helper.add_input(Submit('submit', 'Submit'))
        self.helper.add_input(Submit('learn more', 'Learn More'))


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

    # password = forms.CharField(
    #     widget=forms.PasswordInput,
    #     label = "password",
    #     max_length = 80,
    #     required = True,
    # )

    upload_file = forms.FileField(
        label="upload_file", 
        max_length=80, 
        required=False
        )
