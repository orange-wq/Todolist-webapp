# Generated by Django 4.2.6 on 2023-10-19 08:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('is_done', models.BooleanField(default=False)),
                ('priority', models.CharField(choices=[('high', 'High'), ('medium', 'Medium'), ('low', 'Low')], default='medium', max_length=10)),
                ('date_added', models.DateTimeField(auto_now=True)),
                ('date', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todoapp.date')),
            ],
        ),
    ]
