from django.contrib import admin
from . import models
# Register your models here.



@admin.register(models.Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['id','user','title','slug','created']
    raw_id_fields = ['user']
    prepopulated_fields = {'slug':['title']}


@admin.register(models.Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ['id','user','question','body']
    raw_id_fields = ['user','question']