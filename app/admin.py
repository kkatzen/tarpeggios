from django.contrib import admin
from app.models import *


class RepInline(admin.TabularInline):
    model = Rep

class SingerInline(admin.StackedInline):
    model = Singer
    extra = 0
    readonly_fields = ('name',)
    fields = ('name',)


class SemesterAdmin(admin.ModelAdmin):
    inlines = [
        RepInline,
       	SingerInline
    ]


admin.site.register(Semester, SemesterAdmin)


admin.site.register(Singer)
admin.site.register(Sidebar)
admin.site.register(Page)
admin.site.register(Song)
admin.site.register(Rep)
