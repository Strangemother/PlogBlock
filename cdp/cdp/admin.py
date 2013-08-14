# Auto Generated with make_admin
# ######################################################## #
# YOU MUST DELETE THE ABOVE STATEMENT                      #
# IF YOU DO NOT WANT ./manage.py change_model <model_name> #
# TO REGENERATE THIS admin.py                              #
# YOUR CHANGES WILL BE OVERWRITTEN                         #
############################################################

from django.contrib import admin
from models import LogFile, Device, Parse

class LogFileAdmin(admin.ModelAdmin):
    list_display = ('created', 'log_file', )
    list_filter = ('created', 'log_file', )
    search_fields = ('created', 'log_file', )
    #fields = ('created', 'log_file', )
    filter_horizontal = ()
    #exclude = (,)

class DeviceAdmin(admin.ModelAdmin):
    list_display = ('device_id', 'entry_address', 'platform', 'capabilities', 'interface', 'outgoing_port', 'hold_time', 'version', 'duplex', 'power_drawn', 'power_management_id', 'power_request_levels', 'management_addresses', )
    list_filter = ('device_id', 'entry_address', 'platform', 'capabilities', 'interface', 'outgoing_port', 'hold_time', 'version', 'duplex', 'power_drawn', 'power_management_id', 'power_request_levels', 'management_addresses', )
    search_fields = ('device_id', 'entry_address', 'platform', 'capabilities', 'interface', 'outgoing_port', 'hold_time', 'version', 'duplex', 'power_drawn', 'power_management_id', 'power_request_levels', 'management_addresses', )
    #fields = ('device_id', 'entry_address', 'platform', 'capabilities', 'interface', 'outgoing_port', 'hold_time', 'version', 'duplex', 'power_drawn', 'power_management_id', 'power_request_levels', 'management_addresses', )
    filter_horizontal = ()
    #exclude = (,)

class ParseAdmin(admin.ModelAdmin):
    list_display = ('created', 'log_file', )
    list_filter = ('created', 'log_file', )
    search_fields = ('created', 'log_file', )
    #fields = ('created', 'log_file', )
    filter_horizontal = ()
    #exclude = (,)



admin.site.register(LogFile, LogFileAdmin)
admin.site.register(Device, DeviceAdmin)
admin.site.register(Parse, ParseAdmin)

