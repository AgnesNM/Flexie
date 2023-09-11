from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import FlexieUsers


class UserInput(forms.ModelForm):
    class Meta:
        model = FlexieUsers
        fields = ('email', 'upload_file')
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control', 'style': 'border: 1px solid'}),
            'upload_file': forms.ClearableFileInput(attrs={'class': 'form-control-file', 'style': 'border: 1px solid'}),
        }

        labels = {
            'email': 'Email Address',
            'upload_file': 'Upload a File',
        }
        
    # def __init__(self, *args, **kwargs):
    #     super(UserInput, self).__init__(*args, **kwargs)
    #     self.helper = FormHelper()
    #     self.helper.form_id = 'id-UserInputForm'
    #     self.helper.form_class = 'blueForms'
    #     self.helper.form_method = 'post'
    #     self.helper.form_action = 'index_view'
    #     self.helper.add_input(Submit('submit', 'Submit'))

    #     self.helper.layout = Layout(
    #         Fieldset(
    #             'email',
    #             'upload_file',
    #         ),
    #         ButtonHolder(
    #             Submit('submit', 'Submit', css_class='button white')
    #         )
    #     )

