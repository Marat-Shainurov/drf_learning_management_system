from datetime import datetime

from users.models import User


def is_user_active(user: User) -> bool:

    if user.last_login:
        now = datetime.now()
        last_login = user.last_login.replace(tzinfo=None)
        time_diff = now - last_login

        if time_diff.days <= 30:
            return True
        else:
            return False
