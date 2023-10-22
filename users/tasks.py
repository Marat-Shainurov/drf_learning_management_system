from celery import shared_task

from users.models import User
from users.services import is_user_active


@shared_task
def check_users_activity():
    users = User.objects.all()

    if users:
        for user in users:
            if not is_user_active(user):
                user.is_active = False
                user.save()
