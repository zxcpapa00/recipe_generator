from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

user_model = get_user_model()


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(max_length=30, required=True,
                               widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

    class Meta:
        model = user_model
        fields = ('username', 'password')


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=128)
    last_name = forms.CharField(max_length=128)
    username = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=200)
    password1 = forms.CharField(max_length=30, widget=forms.PasswordInput())
    password2 = forms.CharField(max_length=30, widget=forms.PasswordInput())

    class Meta:
        model = user_model
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')
