# Generated by Django 3.2.7 on 2022-11-25 16:10

import app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0051_playlist_playlist_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='something',
            name='comment_id',
            field=models.CharField(blank=True, default=app.models.random_commentid_generator, max_length=255, null=True),
        ),
    ]