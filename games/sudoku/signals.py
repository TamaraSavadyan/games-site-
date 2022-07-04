from django.dispatch import receiver
from django.db.models.signals import pre_save
from .models import Sudoku
from accounts.models import Account

@receiver(pre_save, sender=Account)
def create_account_sudoku(sender, instance, **kwargs):
    Sudoku.objects.create(account=instance)

@receiver(pre_save, sender=Account)
def save_account_sudoku(sender, instance, **kwargs):
    instance.sudoku.save()        