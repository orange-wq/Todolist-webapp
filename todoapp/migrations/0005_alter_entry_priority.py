# Generated by Django 4.2.6 on 2023-10-19 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0004_alter_entry_priority'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='priority',
            field=models.CharField(choices=[('High', 'High'), ('Medium', 'Medium'), ('Low', 'Low')], default='medium', max_length=10),
        ),
    ]