from django.db import models

# Create your models here.
class MineSweeper(models.Model):
    id = models.AutoField(primary_key=True)
    win_rate = models.IntegerField()
    time = models.TimeField()
    difficulty = models.CharField(max_length=20)

    account = models.ForeignKey("accounts.Account", on_delete=models.CASCADE, related_name='minesweeper_game')

    class Meta:
        db_table = 'minesweeper'

    def __str__(self):
        return self.account
