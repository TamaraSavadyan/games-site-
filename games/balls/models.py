from django.db import models
import sys
sys.path.append('/home/tamara/Desktop/games/games/accounts')
from accounts.models import Account

# Create your models here.
class Balls(models.Model):
    id = models.AutoField(primary_key=True)
    score = models.IntegerField()
    time = models.TimeField()

    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    class Meta:
        db_table = 'balls'

    def __str__(self):
        return self.account   