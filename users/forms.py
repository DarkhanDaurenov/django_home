from django.contrib.auth.forms import UserCreationForm


from catalog.forms import StyleFormsMixin
from users.models import User


class UserRegisterForm(StyleFormsMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2',)



