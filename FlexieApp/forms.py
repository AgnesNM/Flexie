from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import FlexieUsers


class UserInput(forms.Form):
    class Meta:
        model = FlexieUsers
        fields = ('email', 'upload_file')
        
    def __init__(self, *args, **kwargs):
        super(UserInput, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-UserInputForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = 'index_view'
        self.helper.add_input(Submit('submit', 'Submit'))

        self.helper.layout = Layout(
            Fieldset(
                'User Input',
                'email',
                'upload_file',
            ),
            ButtonHolder(
                Submit('submit', 'Submit', css_class='button white')
            )
        )



