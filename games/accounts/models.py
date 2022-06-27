# import sys
# sys.path.append('/home/tamara/Desktop/games-site-/games/balls')
# sys.path.append('/home/tamara/Desktop/games-site-/games/minesweeper')
# sys.path.append('/home/tamara/Desktop/games-site-/games/sudoku')
# sys.path.append('/home/tamara/Desktop/games-site-/games/wordle')
from balls.models import Balls
from minesweeper.models import MineSweeper
from sudoku.models import Sudoku
from wordle.models import Wordle

from django.db import models
from django.contrib.auth.models import User 
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Account(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=0)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    info = models.TextField(blank=True)
    profile_pic = models.ImageField(blank=True)


    balls = models.OneToOneField(Balls, on_delete=models.CASCADE, related_name='user_account')
    minesweeper = models.OneToOneField(MineSweeper, on_delete=models.CASCADE, related_name='user_account')
    sudoku = models.OneToOneField(Sudoku, on_delete=models.CASCADE, related_name='user_account')
    wordle = models.OneToOneField(Wordle, on_delete=models.CASCADE, related_name='user_account')

    class Meta:
        db_table = 'accounts'

    def __str__(self):
        return self.user

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Account.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()