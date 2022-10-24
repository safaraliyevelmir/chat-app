from django.contrib import admin
from .models import *


admin.site.register(Friends)
admin.site.register(CustomUser)
admin.site.register(BlockedList)

