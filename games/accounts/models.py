from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.
class Account(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=200)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=50, 
                                validators=[MinLengthValidator(8, 'Password must contain more than 8 characters')])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'accounts'

    def __str__(self):
        return self.email