# Generated by Django 3.0.5 on 2020-04-16 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='photo',
            field=models.CharField(default='No photo', max_length=50),
        ),
    ]
