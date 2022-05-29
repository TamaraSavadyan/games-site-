import sys
sys.path.append('/home/tamara/Desktop/games-site-/games/balls')
sys.path.append('/home/tamara/Desktop/games-site-/games/minesweeper')
sys.path.append('/home/tamara/Desktop/games-site-/games/sudoku')
sys.path.append('/home/tamara/Desktop/games-site-/games/wordle')
from balls.models import Balls
from minesweeper.models import MineSweeper
from sudoku.models import Sudoku
from wordle.models import Wordle

from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=200)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=50, 
                                validators=[MinLengthValidator(8, 'Password must contain more than 8 characters')])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    balls = models.ForeignKey(Balls, on_delete=models.CASCADE)
    minesweeper = models.ForeignKey(MineSweeper, on_delete=models.CASCADE)
    sudoku = models.ForeignKey(Sudoku, on_delete=models.CASCADE)
    wordle = models.ForeignKey(Wordle, on_delete=models.CASCADE)

    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.email