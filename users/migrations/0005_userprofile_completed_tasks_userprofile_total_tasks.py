# Generated by Django 4.2.7 on 2023-12-16 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_remove_userprofile_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='completed_tasks',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='total_tasks',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
