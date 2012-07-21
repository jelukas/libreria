from django.contrib import admin

from gestion.models import Libro
from gestion.models import Categoria
from gestion.models import Autor

admin.site.register(Libro)
admin.site.register(Categoria)
admin.site.register(Autor)