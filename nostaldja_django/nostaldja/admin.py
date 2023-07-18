from django.contrib import admin
from .models import Fad
from .models import Decade

# Register your models here.
admin.site.register(Fad)
admin.site.register(Decade)