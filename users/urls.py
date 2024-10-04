from django.urls import path, include

from users.views import UserCreateView

urlpatterns = [
    path('api/register', UserCreateView.as_view(), name='register'),
]