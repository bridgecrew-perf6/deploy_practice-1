from dataclasses import fields
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class UserCreateForm(UserCreationForm):

    class Meta:
        model = get_user_model()

        # 'password2' is "confirm password" field
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        # Calling base class contructor
        super().__init__(*args, **kwargs)

        # Custom field labels for the form
        self.fields['username'].label = 'Display name'
        self.fields['email'].label = 'Email Address'