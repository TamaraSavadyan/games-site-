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
from django.core.validators import MinLengthValidator

# Create your models here.
class Account(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=200, unique=True)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=50, 
                                validators=[MinLengthValidator(8, 'Password must contain more than 8 characters')])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    balls = models.ForeignKey(Balls, default=None, on_delete=models.CASCADE, related_name='user_account')
    minesweeper = models.ForeignKey(MineSweeper, default=None, on_delete=models.CASCADE, related_name='user_account')
    sudoku = models.ForeignKey(Sudoku, default=None, on_delete=models.CASCADE, related_name='user_account')
    wordle = models.ForeignKey(Wordle, default=None, on_delete=models.CASCADE, related_name='user_account')

    class Meta:
        db_table = 'accounts'

    def __str__(self):
        return self.email