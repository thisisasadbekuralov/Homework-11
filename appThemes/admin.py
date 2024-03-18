from django.contrib import admin

# Register your models here.

from appThemes.models import Themes, Category

admin.site.register(Themes)
admin.site.register(Category)