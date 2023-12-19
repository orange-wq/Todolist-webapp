from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    help = 'Creates a superuser with is_active=True'

    def handle(self, *args, **options):
        User = get_user_model()
        email = 'bator.tsengel2015@yandex.com'
        password = 'em9PhieW'
        User.objects.create_superuser(email=email, password=password, is_active=True)
        self.stdout.write(self.style.SUCCESS('Superuser created successfully'))
