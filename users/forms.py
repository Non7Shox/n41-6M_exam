from django import forms
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class RegistrationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirm', widget=forms.PasswordInput)

    class Meta:
        model = UserModel
        fields = ('username', 'email', 'first_name', 'last_name')


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()


class LogoutForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
