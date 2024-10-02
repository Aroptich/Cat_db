from django.db import models

from cats.models.breed import Breed
from users.models.users import User


class Cat(models.Model):
    name = models.CharField(max_length=60)
    owner = models.ForeignKey(User,
                              on_delete=models.CASCADE)
    color = models.CharField(max_length=120,
                             blank=True)
    age = models.PositiveIntegerField(blank=False)
    discriprion = models.TextField(max_length=250,
                                   blank=True)
    breed = models.ForeignKey(Breed,
                              on_delete=models.PROTECT,
                              blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Кот'
        verbose_name_plural = 'Коты'
