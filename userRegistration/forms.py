from django import forms
from django.contrib.auth.models import User

class ResistrationForm(forms.Form):
        first_name      = forms.CharField(max_length=120, label= 'First Name')
        last_name       = forms.CharField(max_length=120, label= 'Last Name')
        username        = forms.CharField(max_length=120, label= 'Username')
        email           = forms.EmailField(max_length=120, label= 'Email')
        # date_of_birth   = forms.DateField(label= 'Date of Birth')
        password1       = forms.CharField(max_length=120, label = 'Password', widget=forms.PasswordInput())
        password2       = forms.CharField(max_length=120, label = 'Retype Password', widget=forms.PasswordInput())

        def clean_password2(self):
                password1 = self.cleaned_data.get('password1')
                password2 = self.cleaned_data.get('password2')
                if password1 and password2:
                    if password1 != password2:
                        raise forms.ValidationError('password_mismatch')
                # password_validation.validate_password(password2, self.user)
                    else:
                        return password2

        def clean_username(self):
            username = self.cleaned_data.get('username')
            if  User.objects.filter(username=username).exists():
                raise forms.ValidationError('Username unavailable!!')
            else:
                return username

        def clean_email(self):
            email = self.cleaned_data.get('email')
            if  User.objects.filter(email=email).exists():
                raise forms.ValidationError('email already registered!!')
            else:
                return email


class LoginForm(forms.Form):
    username        = forms.CharField(max_length=120, label= 'Username')
    password       = forms.CharField(max_length=120, label = 'Password', widget=forms.PasswordInput())
