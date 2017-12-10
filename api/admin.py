from django.contrib import admin

from .models import AppInfo
from .models import UserInfo
from .models import LocationData


admin.site.register(AppInfo)
admin.site.register(UserInfo)
admin.site.register(LocationData)