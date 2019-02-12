from django.contrib import admin
from core.models import ProviderProfile, Course, Provider, CourseStatus, UserProfile, TimelineItem


class CourseStatusAdmin(admin.ModelAdmin):
    list_display = ('profile', 'course', 'status')
    list_filter = ('status', 'course')


class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'provider', 'url', 'tag_list')
    list_filter = ('provider',)

    def get_queryset(self, request):
        return super(CourseAdmin, self).get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        return u", ".join(o.name for o in obj.tags.all())


class ProviderProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'username_provider', 'provider')
    list_filter = ('provider',)


class BioAdmin(admin.ModelAdmin):
    list_display = ('user', 'birth_date')


admin.site.register(ProviderProfile, ProviderProfileAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Provider)
admin.site.register(TimelineItem)
admin.site.register(UserProfile, BioAdmin)
admin.site.register(CourseStatus, CourseStatusAdmin)
