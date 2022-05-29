import sys
sys.path.append('/home/tamara/Desktop/games-site-/games/users')
from users.models import User
from django.db import models
from django.conf import settings # for 'settings.AUTH_USER' (if_authenticated)

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

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'wordle'

    def __str__(self):
        return self.user