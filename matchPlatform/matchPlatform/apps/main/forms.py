from django import forms

class RegistrationForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100, widget=forms.TextInput(attrs={
            'placeholder': 'example',
            'autocomplete': 'off',
            'class': 'input-field-input',
            'id': 'nickname'
        }))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={
            'placeholder': "We won't tell anyone",
            'autocomplete': 'off',
            'class': 'input-field-input',
            'id': 'pass'
        }))
    confirm_password = forms.CharField(label='Confirm Password',  widget=forms.PasswordInput(attrs={
            'placeholder': "We won't tell anyone",
            'autocomplete': 'off',
            'class': 'input-field-input',
            'id': 'pass_repeat'
        }))