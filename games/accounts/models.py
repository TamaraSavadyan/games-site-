'''
import sys
sys.path.append('/home/tamara/Desktop/games-site-/games/balls')
sys.path.append('/home/tamara/Desktop/games-site-/games/minesweeper')
sys.path.append('/home/tamara/Desktop/games-site-/games/sudoku')
sys.path.append('/home/tamara/Desktop/games-site-/games/wordle')
'''

from django.db import models
from django.contrib.auth.models import User
from PIL import Image



# Create your models here
class Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    profile_pic = models.ImageField(default='default.png', upload_to='account_images')
    info = models.TextField(null=True)
    
    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.profile_pic.path)
        
        if img.height > 100 or img.width > 100:
            new_img = (100, 100)
            img.thumbnail(new_img)
            img.save(self.profile_pic.path)

    class Meta:
        db_table = 'accounts'

