from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        email = 'takishevdarkhan@gmail.com'
        password = '87014254045'

        user, created = User.objects.get_or_create(email=email)
        user.set_password(password)
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save()
