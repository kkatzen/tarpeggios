from django.contrib import admin
from app.models import *


class RepInline(admin.TabularInline):
    model = Rep
class MemberInline(admin.TabularInline):
    model = Membership

"""
class SingerInline(admin.StackedInline):
    model = Singer
    extra = 0
    readonly_fields = ('name',)
    fields = ('name',)
"""

class SemesterAdmin(admin.ModelAdmin):
    inlines = [
        RepInline,MemberInline
       #	SingerInline
    ]


admin.site.register(Semester, SemesterAdmin)


admin.site.register(Singer)
admin.site.register(Officer)
admin.site.register(Sidebar)
admin.site.register(Page)
admin.site.register(Song)
admin.site.register(Rep)
admin.site.register(Document)
