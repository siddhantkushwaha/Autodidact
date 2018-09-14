from django.contrib.auth.models import User
from django.forms import ModelForm


# class SignUpForm(ModelForm):
#     class Meta:
#         model = User
#         fields = ['first_name', 'username', 'email', 'password']


class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
