from django.contrib import admin

from .models import AppInfo
from .models import UserInfo

admin.site.register(AppInfo)
admin.site.register(UserInfo)
