from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
    """User creation form."""

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
