
from rest_framework import generics, status, permissions
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from cats.models.breed import Breed
from cats.models.cats import Cat
from cats.serializers.breed_serializer import BreedSerializer
from cats.serializers.cat_serializer import CatSerializer
from filters.breed_filter import CatFilter


class CatView(ModelViewSet):
    """Класс представления котенка"""

    queryset = Cat.objects.all()
    serializer_class = CatSerializer
    permission_classes = [permissions.AllowAny,]
    filter_backends = (DjangoFilterBackend,)
    filterset_class = CatFilter


class BreedView(generics.ListAPIView):
    """Получение списка пород"""
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer
    permission_classes = [permissions.AllowAny]