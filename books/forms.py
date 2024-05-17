from django import forms


class TestForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField()
