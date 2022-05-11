from django.contrib import admin
from Questions.models import Event

class EventAdmin(admin.ModelAdmin):
    list_display    = ('event','autor', 'date'  , 'priority' , 'resume')
    list_filter     = ('priority' , 'date')
    list_editable   = ('priority' , )
    search_fields   = ('event' , 'date')
admin.site.register(Event, EventAdmin)





