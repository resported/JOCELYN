from django.forms import ModelForm
from .models import User


class NewUserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']


