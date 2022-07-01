from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import MineSweeper


@receiver(post_save, sender="accounts.Account")
def create_account_minesweeper(sender, instance, created, **kwargs):
    if created:
        MineSweeper.objects.create(account=instance, id=instance.id)

@receiver(post_save, sender="accounts.Account")
def save_account_minesweeper(sender, instance, **kwargs):
    instance.minesweeper.save()