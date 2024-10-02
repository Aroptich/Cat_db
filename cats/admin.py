from django.contrib import admin

from .models.breed import Breed
from .models.cats import Cat

admin.site.register(Cat)
admin.site.register(Breed)
