from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Sudoku
from accounts.models import Account


@receiver(post_save, sender=Account)
def create_account_sudoku(sender, instance, **kwargs):
    if kwargs['created']:
        Sudoku.objects.create(account=instance).save()

     