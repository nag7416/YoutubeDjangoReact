# Generated by Django 3.2.7 on 2022-11-07 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0044_alter_something_comment_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='something',
            name='comment_liked',
            field=models.BooleanField(default=False),
        ),
    ]