# Generated by Django 4.2.6 on 2023-11-08 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0008_entry_image_alter_entry_end_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='date',
            name='title',
            field=models.DateField(),
        ),
    ]
