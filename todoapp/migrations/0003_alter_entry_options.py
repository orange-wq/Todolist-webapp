# Generated by Django 4.2.6 on 2023-10-19 08:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0002_entry'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='entry',
            options={'verbose_name_plural': 'Entries'},
        ),
    ]