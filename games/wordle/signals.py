from django.dispatch import receiver
from django.db.models.signals import pre_save
from .models import Wordle
from accounts.models import Account

@receiver(pre_save, sender=Account)
def create_account_wordle(sender, instance, **kwargs):
    Wordle.objects.create(account=instance)

@receiver(pre_save, sender=Account)
def save_account_wordle(sender, instance, **kwargs):
    instance.wordle.save()    