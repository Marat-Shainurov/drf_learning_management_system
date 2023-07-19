from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

NULLABLE = {'blank': True, 'null': True}


class UserRoles(models.TextChoices):
    MODERATOR = 'moderator', _('moderator')
    MEMBER = 'member', _('member')


class User(AbstractUser):
    username = None
    email = models.EmailField(verbose_name='user_email', max_length=100, unique=True)
    phone = models.CharField(verbose_name='user_phone', max_length=50, **NULLABLE)
    avatar = models.ImageField(verbose_name='users_avatar', upload_to='avatars/', **NULLABLE)
    city = models.CharField(verbose_name='user_city', max_length=250, **NULLABLE)
    role = models.CharField(choices=UserRoles.choices, max_length=10, verbose_name='user_role',
                            default=UserRoles.MEMBER)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def delete(self, **kwargs):
        self.is_active = False
        self.save()
