from django.contrib import admin

from locking.models import Lock

class LockAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_on'
    list_display = ('locked_object', 'created_on')
admin.site.register(Lock, LockAdmin)
