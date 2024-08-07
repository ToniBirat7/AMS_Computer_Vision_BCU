from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class' : 'input', 'maxlength' : '100', 'placeholder' : 'Enter Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'input', 'maxlength' : '100', 'placeholder' : 'Enter Password'}))

    