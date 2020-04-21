# Generated by Django 3.0.5 on 2020-04-15 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('photo', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('director', models.CharField(max_length=30)),
                ('genres', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=5)),
                ('year', models.CharField(max_length=4)),
                ('imdb_score', models.DecimalField(decimal_places=2, max_digits=9)),
                ('imdb_link', models.URLField(default='')),
                ('poster', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('slug', models.SlugField(default='Default', unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('actors', models.ManyToManyField(to='movie.Actor')),
            ],
        ),
    ]
