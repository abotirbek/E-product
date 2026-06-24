from django import forms
from .models import CustomUser

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = [
            'username',
            'email',
            'phone',
            'password',
        ]

    def save(self, commit = True, **kwargs):
        return CustomUser.objects.create_user(
            username=self.cleaned_data.get('username'),
            email=self.cleaned_data.get('email'),
            password=self.cleaned_data.get('password'),
            phone=self.cleaned_data.get('phone'),
        )

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(max_length=150)