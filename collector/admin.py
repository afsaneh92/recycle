from django.contrib import admin
from .models import Receiver, MobileUser, RecyclingRequest
from . import models


class ReceiverAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'mobile_number', 'manager')


class MobileUserAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'mobile_number')


class RecyclingRequestAdmin(admin.ModelAdmin):
    list_display = ('requester', 'receiver','status', 'trash_type', 'address')
    list_filter = ('status', 'trash_type')


admin.site.register(Receiver, ReceiverAdmin)
admin.site.register(MobileUser, MobileUserAdmin)
admin.site.register(RecyclingRequest, RecyclingRequestAdmin)