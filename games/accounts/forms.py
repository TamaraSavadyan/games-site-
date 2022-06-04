from django.forms import ModelForm
from .models import Account

# Create the form class.
class ArticleForm(ModelForm):
    class Meta:
        model = Account
        fields = ['email', 'name', 'password']