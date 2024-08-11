from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class' : 'input', 'maxlength' : '100', 'placeholder' : 'Enter Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'input', 'maxlength' : '100', 'placeholder' : 'Enter Password'}))

    # def clean_username(self):
    #     uname = self.cleaned_data.get('username')
    #     if len(uname) <= 5 and ' ' in uname:
    #         raise forms.ValidationError('Username must be more than 5 characters and should not contain spaces')
    #     return uname
    
    # def clean_password(self):
    #     pwd = self.cleaned_data.get('password')
    #     if '$' not in pwd:
    #         raise forms.ValidationError('Password Must Contain $')
    #     return pwd
    
   