from rest_framework import serializers

from users.models.users import User


class RegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(min_length=8, write_only=True)

    def create(self, validated_data):
        """Создаем хешируемый пароль пользователя"""
        password = validated_data.pop("password")
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

    class Meta:
        model = User
        fields = ['email',
                   'password']


class UserSerializer(serializers.ModelSerializer):
    """Серализация email пользователя"""
    class Meta:
        model = User
        fields = ['email']