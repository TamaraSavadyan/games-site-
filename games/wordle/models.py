from django.db import models
from django.conf import settings # for 'settings.AUTH_USER_MODEL' (if_authenticated)

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

    account = models.ForeignKey("accounts.Account", on_delete=models.CASCADE, related_name='wordle_game')

    class Meta:
        db_table = 'wordle'

    def __str__(self):
        return self.account