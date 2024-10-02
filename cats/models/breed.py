from django.db import models

class Breed(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Порода'
        verbose_name_plural = 'Породы'