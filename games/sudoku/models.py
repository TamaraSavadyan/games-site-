from django.db import models


# Create your models here.
class Sudoku(models.Model):
    win_rate = models.IntegerField(null=True)
    time = models.TimeField(null=True)
    dificulty = models.CharField(max_length=20, null=True)

    account = models.ForeignKey("accounts.Account", on_delete=models.CASCADE, related_name='sudoku_game')

    class Meta:
        db_table = 'sudoku'


