from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Wordle
from accounts.models import Account


@receiver(post_save, sender=Account)
def create_account_wordle(sender, instance, **kwargs):
    if kwargs['created']:
        Wordle.objects.create(account=instance).save()
