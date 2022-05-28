from django.db import models
from django.conf import settings
import sys
sys.path.append('/home/tamara/Desktop/games/games/accounts')
from accounts.models import Account


# Create your models here.
class Wordle(models.Model):
    id = models.AutoField(primary_key=True)
    win_rate = models.IntegerField()
    time_completion = models.TimeField()

    times_played = models.IntegerField(default=0)
    first_try = models.IntegerField()
    second_try = models.IntegerField()
    three_try = models.IntegerField()
    fourth_try = models.IntegerField()
    fifth_try = models.IntegerField()
    sixth_try = models.IntegerField()

    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    class Meta:
        db_table = 'wordle'

    def __str__(self):
        return self.account