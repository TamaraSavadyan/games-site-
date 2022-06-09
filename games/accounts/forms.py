from django.forms import ModelForm
from .models import Account


class AccountCreateForm(ModelForm):
	class Meta:
		model = Account
		fields = ['email', 'username', 'password']
		

class AccountLoginForm(ModelForm):
	class Meta:
		model = Account
		fields = ['email', 'password']		
