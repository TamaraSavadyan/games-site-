from django.dispatch import receiver
from django.db.models.signals import pre_save
from .models import Balls
from accounts.models import Account

@receiver(pre_save, sender=Account)
def create_account_balls(sender, instance, **kwargs):
    Balls.objects.create(account=instance)

@receiver(pre_save, sender=Account)
def save_account_balls(sender, instance, **kwargs):
    instance.balls.save()