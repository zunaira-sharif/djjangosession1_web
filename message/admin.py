from django.contrib import admin
from .models import query

class queryadmin(admin.ModelAdmin):
    list_display=['Name','Email','Subject','Contact','Message']
      
admin.site.register(query,queryadmin)
# Register your models here.
