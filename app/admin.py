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


class SingerAdmin(admin.ModelAdmin):
    list_filter = ('graduation_semester','voice_part')

class RepAdmin(admin.ModelAdmin):
    list_filter = ('semester',)

class SemesterAdmin(admin.ModelAdmin):
    inlines = [
        MemberInline,RepInline
       #	SingerInline
    ]


admin.site.register(Semester, SemesterAdmin)
admin.site.register(Singer, SingerAdmin)
admin.site.register(Rep, RepAdmin)

admin.site.register(Event)

admin.site.register(Officer)
admin.site.register(Sidebar)
admin.site.register(Page)
admin.site.register(Song)
admin.site.register(Document)
