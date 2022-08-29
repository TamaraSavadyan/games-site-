from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save
from .models import Balls
from accounts.models import Account

# # @receiver(post_save, sender=Account)
# # def my_handler(sender, **kwargs):
# #     if sender.pk:  # create
# #         sender.model = Balls.objects.create(balls_id=sender.pk)

@receiver(post_save, sender=Account)
def create_account_balls(sender, instance, **kwargs):
    if kwargs['created']:
        Balls.objects.create(account=instance).save()


    