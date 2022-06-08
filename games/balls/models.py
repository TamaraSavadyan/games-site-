from django.db import models

# Create your models here.
class Balls(models.Model):
    id = models.AutoField(primary_key=True)
    score = models.IntegerField(null=True)
    time = models.TimeField(null=True)

    account = models.OneToOneField("accounts.Account", on_delete=models.CASCADE, related_name='balls_game')

    class Meta:
        db_table = 'balls'

    def __str__(self):
        return self.account   