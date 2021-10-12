from django.contrib import admin
from . import models
# Register your models here.
@admin.register(models.User)
class Useradmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'password')