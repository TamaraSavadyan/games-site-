from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Wordle

@receiver(post_save, sender="accounts.Account")
def create_account_wordle(sender, instance, created, **kwargs):
    if created:
        Wordle.objects.create(account=instance, id=instance.id)

@receiver(post_save, sender="accounts.Account")
def save_account_wordle(sender, instance, **kwargs):
    instance.wordle.save()    