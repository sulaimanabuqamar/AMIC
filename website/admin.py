from django.contrib import admin
from .models import Timeline, head, committee, member, advisor, Photo, aboutUsPhoto, Activity

# Register your models here.

class activityAdmin(admin.ModelAdmin):
    list_display = ['activity_name', 'activity', 'date', 'location']
    search_fields = ['activity_name', 'date']

class timelineAdmin(admin.ModelAdmin):
    list_display = ['timeline_id', 'start_year', 'end_year']
    search_fields = ['start_year', 'end_year']
    
class headAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'role', 'team_type']
    search_fields = ['name', 'role']

class committeeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'role', 'amicoins', 'team_type']
    search_fields = ['name', 'role']
    
class memberAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'amicoins', 'team_type']
    search_fields = ['name']
    
class advisorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'role']
    search_fields = ['name', 'role']
    
class photoAdmin(admin.ModelAdmin):
    list_display = ['image', 'activity']
    search_fields = ['image', 'activity']
    
class aboutUsPhotosAdmin(admin.ModelAdmin):
    list_display = ['image1', 'image2', 'image3']


admin.site.register(Activity, activityAdmin)
admin.site.register(Timeline, timelineAdmin)
admin.site.register(head, headAdmin)
admin.site.register(committee, committeeAdmin)
admin.site.register(member, memberAdmin)
admin.site.register(advisor, advisorAdmin)
admin.site.register(aboutUsPhoto, aboutUsPhotosAdmin)
admin.site.register(Photo, photoAdmin)