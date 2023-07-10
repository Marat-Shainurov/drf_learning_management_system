from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}

class User(AbstractUser):
    username = None
    email = models.EmailField(verbose_name='user_email', max_length=100, unique=True)
    phone = models.CharField(verbose_name='user_phone', max_length=50, **NULLABLE)
    avatar = models.ImageField(verbose_name='users_avatar', upload_to='avatars/', **NULLABLE)
    city = models.CharField(verbose_name='user_city', max_length=250, **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def delete(self, **kwargs):
        self.is_active = False
        self.save()


