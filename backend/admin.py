from django.contrib import admin
from . import models

admin.site.register(models.Post)
admin.site.register(models.Agent)
admin.site.register(models.Lead)