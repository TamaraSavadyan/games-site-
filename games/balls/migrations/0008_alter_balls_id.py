# Generated by Django 4.0.4 on 2022-06-30 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('balls', '0007_balls_account'),
    ]

    operations = [
        migrations.AlterField(
            model_name='balls',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
