from rest_framework import serializers

from cats.models.cats import Cat
from cats.serializers.breed_serializer import BreedSerializer
from users.serializers import UserSerializer


class CatSerializer(serializers.ModelSerializer):
    """Создание котенка"""

    owner = UserSerializer()
    breed = BreedSerializer()

    class Meta:
        model = Cat
        fields = ['id',
                  'name',
                  'owner',
                  'breed',
                  'discriprion',
                  'color',
                  'age']