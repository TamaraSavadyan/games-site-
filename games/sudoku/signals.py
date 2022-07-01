from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Sudoku

@receiver(post_save, sender="accounts.Account")
def create_account_sudoku(sender, instance, created, **kwargs):
    if created:
        Sudoku.objects.create(account=instance, id=instance.id)

@receiver(post_save, sender="accounts.Account")
def save_account_sudoku(sender, instance, **kwargs):
    instance.sudoku.save()        