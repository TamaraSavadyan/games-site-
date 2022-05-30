from django.db import models

# Create your models here.
class Sudoku(models.Model):
    id = models.AutoField(primary_key=True)
    win_rate = models.IntegerField()
    time = models.TimeField()
    dificulty = models.CharField(max_length=20)

    account = models.ForeignKey("accounts.Account", on_delete=models.CASCADE, related_name='sudoku_game')

    class Meta:
        db_table = 'sudoku'

    def __str__(self):
        return self.account