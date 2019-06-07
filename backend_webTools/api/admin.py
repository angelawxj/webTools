from django.contrib import admin

# Register your models here.
from .models import Report, Interview

admin.site.register(Report)
admin.site.register(Interview)