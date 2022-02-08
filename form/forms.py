from django import forms
from django.core.exceptions import ValidationError

def length_check(length):
    def check_length(value):
        if len(value) < length:
            raise ValidationError(('This field needs to be %(length)s characters long'), params={'length': length}, code='invalid')
    return check_length
    
class EnterForm(forms.Form):
    user_name = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput(), validators = [])

class DateInput(forms.DateInput):
    input_type = 'date'

class LoginForm(forms.Form):
    user_name = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput(), validators = [])

class RegisterForm(forms.Form):
    user_name = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput(), validators = [])
    birth_date = forms.DateField(label="Birth Date", widget=DateInput())
    email = forms.EmailField(label='Email', widget=forms.EmailInput())

class ChatForm(forms.Form):
    comment=forms.CharField(widget=forms.Textarea, max_length=1000)

   