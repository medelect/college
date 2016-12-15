from django.contrib import admin
from students.models import Group, Student


class StudentInline(admin.TabularInline):
    model = Student
    extra = 3 


class GroupAdmin(admin.ModelAdmin):
    fields = ['name', 'warden']
    inlines = [StudentInline]

class StudentAdmin(admin.ModelAdmin):
#    fields = ['full_name','birthday','student_card','st_group']
    fieldsets = [
             ('Personal',             {'fields': ['full_name', 'birthday']}),
             ('Official information', {'fields': ['student_card']}),
             (None,                   {'fields': ['st_group']}),
            ]




admin.site.register(Group, GroupAdmin)
admin.site.register(Student, StudentAdmin)
