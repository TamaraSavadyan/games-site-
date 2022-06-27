from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User

# Create your models here.
class Balls(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    score = models.IntegerField(null=True)
    time = models.TimeField(null=True)

    account = models.OneToOneField("accounts.Account", on_delete=models.CASCADE, related_name='balls_game')
    
    @receiver(post_save, sender="accounts.Account")
    def balls_create(sender, instance=None, created=False, **kwargs):
        if created:
            Balls.objects.create(user=instance,)
    
    class Meta:
        db_table = 'balls'

    def __str__(self):
        return self.account   