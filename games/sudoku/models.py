from django.db import models

# Create your models here.
class Sudoku(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    win_rate = models.IntegerField(null=True)
    time = models.TimeField(null=True)
    dificulty = models.CharField(max_length=20, null=True)

    account = models.OneToOneField("accounts.Account", on_delete=models.CASCADE, related_name='sudoku_game')

    @classmethod
    def create(cls, id):
        sudoku = cls(id=id)
        return sudoku

    class Meta:
        db_table = 'sudoku'

    def __str__(self):
        return self.account