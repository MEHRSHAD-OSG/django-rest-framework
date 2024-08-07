from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from . import models
# Register your models here.


@admin.register(models.Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id','user','bio','age']
    raw_id_fields = ['user']