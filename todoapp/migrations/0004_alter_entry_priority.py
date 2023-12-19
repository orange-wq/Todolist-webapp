# Generated by Django 4.2.6 on 2023-10-19 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0003_alter_entry_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='priority',
            field=models.CharField(choices=[('High', 'high'), ('Medium', 'medium'), ('Low', 'low')], default='medium', max_length=10),
        ),
    ]
