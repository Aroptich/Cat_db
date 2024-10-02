from rest_framework import serializers

from cats.models.breed import Breed


class BreedSerializer(serializers.ModelSerializer):
    """Сериализация название породы котенка"""

    class Meta:
        model = Breed
        fields = ['name']