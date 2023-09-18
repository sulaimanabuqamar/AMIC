from django.contrib import admin
from .models import Timeline, headTeam, organizingcommitteeTeam, memberTeam, advisorTeam

# Register your models here.

class timelineAdmin(admin.ModelAdmin):
    list_display = ['timeline_id', 'activity', 'activity_name', 'date', 'location']
    search_fields = ['activity_name', 'date']
    
class headTeamAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'role', 'about']
    search_fields = ['name', 'role']

class organizingcommitteeTeamAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'role', 'about']
    search_fields = ['name', 'role']
    
class memberTeamAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'role', 'about']
    search_fields = ['name', 'role']
    
class advisorTeamAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'role', 'about']
    search_fields = ['name', 'role']

admin.site.register(Timeline, timelineAdmin)
admin.site.register(headTeam, headTeamAdmin)
admin.site.register(organizingcommitteeTeam, organizingcommitteeTeamAdmin)
admin.site.register(memberTeam, memberTeamAdmin)
admin.site.register(advisorTeam, advisorTeamAdmin)
