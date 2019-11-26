from django.contrib import admin

# Register your models here.
from .models import Home, About

admin.site.register(Home)
admin.site.register(About)