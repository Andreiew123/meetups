from django.contrib import admin
from .models import Meetup, Location, Participant

# class MeetupAdmin(admin.ModelAdmin):
                  
admin.site.register(Meetup)
admin.site.register(Location)
admin.site.register(Participant)