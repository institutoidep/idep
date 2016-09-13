from django.contrib import admin

from .models import Area_Estudio
from .models import Alumno
from .models import Horario

admin.site.register(Area_Estudio)
admin.site.register(Alumno)
admin.site.register(Horario)