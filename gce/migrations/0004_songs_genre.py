# Generated by Django 3.2.3 on 2021-06-09 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gce', '0003_songs_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='songs',
            name='genre',
            field=models.CharField(default='NULL', max_length=100),
        ),
    ]