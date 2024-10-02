from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import generics, permissions, status
from rest_framework.response import Response

from users.serializers import RegistrationSerializer

@extend_schema_view(
    post=extend_schema(summary='Регистрация пользователя', tags=['Аутентификация & Авторизация']),
    get=extend_schema(summary='Получение данных пользователя', tags=['Аутентификация & Авторизация'])
)
class UserCreateView(generics.CreateAPIView):
    """Оправляет POST запрос для регистрации пользователя в БД"""
    serializer_class = RegistrationSerializer
    permission_classes = [permissions.AllowAny]  # Создать пользователя могут не авторизированные пользователи

    def post(self, request, *args, **kwargs):
        """Метод возвращает статус POST запроса"""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(status=status.HTTP_201_CREATED)