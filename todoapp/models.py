from django.db import models
from django.conf import settings
from datetime import time


class Date(models.Model):
    title = models.DateField()
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Entry(models.Model):

    PRIORITY_CHOICES = [
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low'),
    ]

    date = models.ForeignKey(Date, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    is_done = models.BooleanField(default=False)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='medium')
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    date_added = models.DateTimeField(auto_now=True)
    start_time = models.TimeField(default=time(0, 00))
    end_time = models.TimeField(default=time(0, 00))

    class Meta:
        verbose_name_plural = 'Entries'

    def __str__(self):
        return self.title
