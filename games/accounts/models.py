'''
import sys
sys.path.append('/home/tamara/Desktop/games-site-/games/balls')
sys.path.append('/home/tamara/Desktop/games-site-/games/minesweeper')
sys.path.append('/home/tamara/Desktop/games-site-/games/sudoku')
sys.path.append('/home/tamara/Desktop/games-site-/games/wordle')
'''
from balls.models import Balls
from minesweeper.models import MineSweeper
from sudoku.models import Sudoku
from wordle.models import Wordle

from django.db import models
from django.contrib.auth.models import User


# Create your models here
class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    info = models.TextField(null=True)
    profile_pic = models.ImageField(null=True)

    # balls = models.OneToOneField(
    #     Balls, on_delete=models.CASCADE, related_name='user_account')
    # minesweeper = models.OneToOneField(
    #     MineSweeper, on_delete=models.CASCADE, related_name='user_account')
    # sudoku = models.OneToOneField(
    #     Sudoku, on_delete=models.CASCADE, related_name='user_account')
    # wordle = models.OneToOneField(
    #     Wordle, on_delete=models.CASCADE, related_name='user_account')

    class Meta:
        db_table = 'accounts'

