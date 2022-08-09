from django.db import models

# Create your models here.
class Balls(models.Model):
    score = models.IntegerField(null=True)
    time = models.TimeField(null=True)

    account = models.ForeignKey("accounts.Account", on_delete=models.CASCADE, related_name='balls_game')

    class Meta:
        db_table = 'balls'


