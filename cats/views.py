from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import generics, permissions
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from cats.models.breed import Breed
from cats.models.cats import Cat
from cats.serializers.breed_serializer import BreedSerializer
from cats.serializers.cat_serializer import CatSerializer
from filters.breed_filter import CatFilter

@extend_schema_view(
    list=extend_schema(summary='Получение списка котят', tags=['Котята']),
    retrieve=extend_schema(summary='Получение информации об 1 котенке', tags=['Котята']),
    update=extend_schema(summary='Полное редактирование котенка', tags=['Котята']),
    partial_update=extend_schema(summary='Частичное редактирование котенка', tags=['Котята']),
    destroy=extend_schema(summary='Удаление котенка', tags=['Котята']),
)
class CatView(ModelViewSet):
    """Класс представления котенка"""

    queryset = Cat.objects.all()
    serializer_class = CatSerializer
    permission_classes = [permissions.AllowAny,]
    filter_backends = (DjangoFilterBackend,)
    filterset_class = CatFilter

@extend_schema_view(
    list=extend_schema(summary='Получение списка пород котят', tags=['Породы']),
)
class BreedView(generics.ListAPIView):
    """Получение списка пород"""
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer
    permission_classes = [permissions.AllowAny]