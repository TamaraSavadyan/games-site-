from django.db import models

# Create your models here.
class Balls(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    score = models.IntegerField(null=True)
    time = models.TimeField(null=True)

    account = models.OneToOneField("accounts.Account", on_delete=models.CASCADE, related_name='balls_game')
    
    @classmethod
    def create(cls, id):
        balls = cls(id=id)
        # do something with the book
        return balls
    
    class Meta:
        db_table = 'balls'

    def __str__(self):
        return self.account   