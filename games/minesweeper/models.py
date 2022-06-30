from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.
class MineSweeper(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    win_rate = models.IntegerField(null=True)
    time = models.TimeField(null=True)
    difficulty = models.CharField(max_length=20, null=True)

    # account = models.OneToOneField("accounts.Account", on_delete=models.CASCADE, related_name='minesweeper_game')

    class Meta:
        db_table = 'minesweeper'


# @receiver(post_save, sender="accounts.Account")
# def create_account_minesweeper(sender, instance, created, **kwargs):
#     if created:
#         MineSweeper.objects.create(account=instance)

# @receiver(post_save, sender="accounts.Account")
# def save_account_minesweeper(sender, instance, **kwargs):
#     instance.minesweeper.save()