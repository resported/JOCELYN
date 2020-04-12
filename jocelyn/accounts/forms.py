from django.forms import ModelForm
from .models import *

"""
class NewUserGroup(ModelForm):
	class Meta:
		nodel = NewUserGroup
		fields = ['title', ]		
"""

class EditProfile(ModelForm):
	model = User