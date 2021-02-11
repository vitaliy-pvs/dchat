from django.contrib import admin
from .models import Message, Settings

admin.site.register(Message)
admin.site.register(Settings)
