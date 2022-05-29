import sys
sys.path.append('/home/tamara/Desktop/games-site-/games/users')
from users.models import User
from django.db import models

# Create your models here.
class Balls(models.Model):
    id = models.AutoField(primary_key=True)
    score = models.IntegerField()
    time = models.TimeField()

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'balls'

    def __str__(self):
        return self.user   