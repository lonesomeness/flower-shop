from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django import forms

from users.models import User

class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email')

class UserProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email')