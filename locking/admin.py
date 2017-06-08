from __future__ import absolute_import
from django.contrib import admin

from .models import NonBlockingLock


class NonBlockingLockAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_on'
    list_display = ('locked_object', 'created_on')


admin.site.register(NonBlockingLock, NonBlockingLockAdmin)
