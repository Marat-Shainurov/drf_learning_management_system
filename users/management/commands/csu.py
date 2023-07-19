from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        user = User(
            email='moderator@mail.ru',
            first_name='New_name',
            last_name='New_surname',
            is_staff=True,
            is_superuser=True,
            is_active=True,
        )
        user.set_password('123')
        user.save()