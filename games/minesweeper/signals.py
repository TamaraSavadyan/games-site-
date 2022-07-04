from django.dispatch import receiver
from django.db.models.signals import pre_save
from .models import MineSweeper
from accounts.models import Account


@receiver(pre_save, sender=Account)
def create_account_minesweeper(sender, instance, **kwargs):
    MineSweeper.objects.create(account=instance)

@receiver(pre_save, sender=Account)
def save_account_minesweeper(sender, instance, **kwargs):
    instance.minesweeper.save()