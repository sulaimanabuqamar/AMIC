from django.contrib import admin
from .models import Timeline, head, committee, member, advisor, Photo, aboutUsPhoto

# Register your models here.

class timelineAdmin(admin.ModelAdmin):
    list_display = ['timeline_id', 'activity_name', 'activity', 'date', 'location']
    search_fields = ['activity_name', 'date']
    
class headAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'role', 'about', 'team_type']
    search_fields = ['name', 'role']

class committeeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'role', 'about', 'amicoins', 'team_type']
    search_fields = ['name', 'role']
    
class memberAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'about', 'amicoins', 'team_type']
    search_fields = ['name']
    
class advisorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'role', 'about']
    search_fields = ['name', 'role']
    
class photoAdmin(admin.ModelAdmin):
    list_display = ['image', 'timeline']
    search_fields = ['image', 'timeline']
    
class aboutUsPhotosAdmin(admin.ModelAdmin):
    list_display = ['image1', 'image2', 'image3']


admin.site.register(Timeline, timelineAdmin)
admin.site.register(head, headAdmin)
admin.site.register(committee, committeeAdmin)
admin.site.register(member, memberAdmin)
admin.site.register(advisor, advisorAdmin)
admin.site.register(aboutUsPhoto, aboutUsPhotosAdmin)
admin.site.register(Photo, photoAdmin)