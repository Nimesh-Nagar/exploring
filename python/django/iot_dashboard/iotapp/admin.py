from django.contrib import admin

from iotapp.models import Device, Sensor 

class DeviceAdmin(admin.ModelAdmin):
    list_display = ('name','description' ,'created_at', 'last_modified', 'is_online') 
    search_fields = ('name',)
    list_per_page = 10 
    actions = ['set_device_offline']

    def set_device_offline(self, request, queryset):
        count = queryset.update(is_online=False)
        self.message_user(request, f"{count} device(s) have been set offline.")
    set_device_offline.short_description = "Set selected devices offline"   

class SensorAdmin(admin.ModelAdmin):
    list_display = ('name', 'device', 'sensor_type')
    list_filter = ('sensor_type', 'device')
    search_fields = ('name', 'device__name')
    list_per_page = 20


# Register your models here.
admin.site.register(Device, DeviceAdmin)
admin.site.register(Sensor, SensorAdmin)


