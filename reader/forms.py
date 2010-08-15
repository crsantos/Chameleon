from django import forms
from reader.models import *

class FriendInviteForm(forms.Form): 
	name = forms.CharField(label='Friend\'s Name')
	email = forms.EmailField(label='Friend\'s Email')
