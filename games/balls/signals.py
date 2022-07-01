from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Balls


@receiver(post_save, sender="accounts.Account")
def create_account_balls(sender, instance, created, **kwargs):
    if created:
        Balls.objects.create(account=instance, id=instance.id)

@receiver(post_save, sender="accounts.Account")
def save_account_balls(sender, instance, **kwargs):
    instance.balls.save()        