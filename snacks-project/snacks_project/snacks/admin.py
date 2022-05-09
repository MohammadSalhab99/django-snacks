from django.contrib import admin
from snacks.models import snack

@admin.register(snack)
class AdminSnack(admin.ModelAdmin):
    pass 

