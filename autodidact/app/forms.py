from django import forms


class SignUpForm(forms.Form):
    username = forms.CharField(label='Username', max_length=20, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    email = forms.EmailField(label='Email', widget=forms.TextInput(attrs={'placeholder': 'Email'}))
