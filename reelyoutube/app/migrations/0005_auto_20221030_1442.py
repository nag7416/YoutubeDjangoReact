# Generated by Django 3.2.7 on 2022-10-30 09:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0004_history'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicalvideo',
            name='author',
        ),
        migrations.RemoveField(
            model_name='historicalvideo',
            name='history_user',
        ),
        migrations.RemoveField(
            model_name='history',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='history',
            name='object_id',
        ),
        migrations.AddField(
            model_name='history',
            name='post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.video'),
        ),
        migrations.AlterField(
            model_name='history',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='HistoricalUser',
        ),
        migrations.DeleteModel(
            name='HistoricalVideo',
        ),
    ]