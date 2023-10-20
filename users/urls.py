from django.urls import path

from users.apps import UsersConfig
from users.views import UsersCreateAPIView, UsersListAPIView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = UsersConfig.name

urlpatterns = [
    path('users/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('users/create/', UsersCreateAPIView.as_view(), name='user_create'),
    path('users/', UsersListAPIView.as_view(), name='user_list'),
]
