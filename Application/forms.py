from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name','last_name','username', 'email', 'password1', 'password2')
        widgets = {
            'password1':forms.PasswordInput(),
            'password2':forms.PasswordInput(),
        }

class UserIdentityForm(forms.Form):
    username = forms.CharField(max_length=150, required=True)
    email = forms.EmailField(required=True)

    
