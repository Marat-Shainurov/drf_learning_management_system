from django.urls import path

from users.apps import UsersConfig
from users.views import UsersRetrieveAPIView, UsersUpdateAPIView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = UsersConfig.name

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('detail/<int:pk>/', UsersRetrieveAPIView.as_view(), name='user_detail'),
    path('update/<int:pk>/', UsersUpdateAPIView.as_view(), name='user_update'),
]
