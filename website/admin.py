from django.contrib import admin
from .models import Timeline, headTeam, committeeTeam, memberTeam, advisorTeam, Photo

# Register your models here.

class timelineAdmin(admin.ModelAdmin):
    list_display = ['timeline_id', 'activity', 'activity_name', 'date', 'location']
    search_fields = ['activity_name', 'date']
    
class headTeamAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'role', 'about']
    search_fields = ['name', 'role']

class committeeTeamAdmin(admin.ModelAdmin):
    list_display = ['id', 'amicoins', 'name', 'role', 'about']
    search_fields = ['name', 'role']
    
class memberTeamAdmin(admin.ModelAdmin):
    list_display = ['id', 'amicoins', 'name', 'about']
    search_fields = ['name', 'role']
    
class advisorTeamAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'role', 'about']
    search_fields = ['name', 'role']
    
class photoAdmin(admin.ModelAdmin):
    list_display = ['image', 'timeline']
    search_fields = ['image', 'timeline']

admin.site.register(Timeline, timelineAdmin)
admin.site.register(headTeam, headTeamAdmin)
admin.site.register(committeeTeam, committeeTeamAdmin)
admin.site.register(memberTeam, memberTeamAdmin)
admin.site.register(advisorTeam, advisorTeamAdmin)
admin.site.register(Photo, photoAdmin)
