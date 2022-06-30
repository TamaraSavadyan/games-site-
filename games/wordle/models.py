from django.db import models
from django.conf import settings # for 'settings.AUTH_USER_MODEL' (if_authenticated)
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.
class Wordle(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    win_rate = models.IntegerField(null=True)
    time_completion = models.TimeField(null=True)

    times_played = models.IntegerField(null=True)
    first_try = models.IntegerField(null=True)
    second_try = models.IntegerField(null=True)
    three_try = models.IntegerField(null=True)
    fourth_try = models.IntegerField(null=True)
    fifth_try = models.IntegerField(null=True)
    sixth_try = models.IntegerField(null=True)

    # account = models.OneToOneField("accounts.Account", on_delete=models.CASCADE, related_name='wordle_game')

    class Meta:
        db_table = 'wordle'

# @receiver(post_save, sender="accounts.Account")
# def create_account_wordle(sender, instance, created, **kwargs):
#     if created:
#         Wordle.objects.create(account=instance)

# @receiver(post_save, sender="accounts.Account")
# def save_account_wordle(sender, instance, **kwargs):
#     instance.wordle.save()                