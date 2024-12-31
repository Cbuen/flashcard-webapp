from django.contrib import admin
from .models import Users, Sets, Cards  # Import your models

admin.site.register(Users)
admin.site.register(Sets)
admin.site.register(Cards)
