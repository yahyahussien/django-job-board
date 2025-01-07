# Generated by Django 4.2.17 on 2025-01-07 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0004_job_published_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='experience',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='job',
            name='salary',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='job',
            name='vacancy',
            field=models.IntegerField(default=1),
        ),
    ]
