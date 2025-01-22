from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django_recaptcha.fields import ReCaptchaField


class CreateUserForm(UserCreationForm):
    """User creation form."""

    captcha = ReCaptchaField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
