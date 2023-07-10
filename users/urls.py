from django.urls import path

from users.apps import UsersConfig
from users.views import UsersRetrieveAPIView, UsersUpdateAPIView

app_name = UsersConfig.name

urlpatterns = [
    path('users/detail/<int:pk>/', UsersRetrieveAPIView.as_view(), name='user_detail'),
    path('users/update/<int:pk>/', UsersUpdateAPIView.as_view(), name='user_update'),
]