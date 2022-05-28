from django.db import models
import sys
sys.path.append('/home/tamara/Desktop/games/games/accounts')
from accounts.models import Account

# Create your models here.
class MineSweeper(models.Model):
    id = models.AutoField(primary_key=True)
    win_rate = models.IntegerField()
    time = models.TimeField()
    difficulty = models.CharField(max_length=20)

    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    class Meta:
        db_table = 'minesweeper'

    def __str__(self):
        return self.account
