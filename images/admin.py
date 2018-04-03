from django.contrib import admin
from . import models #모델임폴트.
# Register your models here.

admin.site.register(models.Image)
admin.site.register(models.Comment)
admin.site.register(models.Like)