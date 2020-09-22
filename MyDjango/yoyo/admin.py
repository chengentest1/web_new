from django.contrib import admin

from yoyo import models

# Register your models here.

class ControlPersionInfo(admin.ModelAdmin):
    list_display = ("id","name","age","qq")
    search_fields = ('name',)
    # search_fields = ('QQ',)

admin.site.register(models.PeronInfo,ControlPersionInfo)
