from django.contrib import admin

from .models import PersonalData, Experience, Education, Skill, DesireRole, AddEducation


# admin.site.register(PersonalData)
# admin.site.register(Experience)
# admin.site.register(Education)
# admin.site.register(Skill)

@admin.register(PersonalData)
class PostAdmin(admin.ModelAdmin):
    list_display = ['fio', 'born', 'city']


@admin.register(Experience)
class PostAdmin(admin.ModelAdmin):
    list_display = ['role', 'data_start', 'data_end','tasks']


@admin.register(Education)
class PostAdmin(admin.ModelAdmin):
    list_display = ['univer', 'data_end']


@admin.register(AddEducation)
class PostAdmin(admin.ModelAdmin):
    list_display = ['univer', 'data_end']


@admin.register(Skill)
class PostAdmin(admin.ModelAdmin):
    list_display = ['about', 'hobbies']


@admin.register(DesireRole)
class PostAdmin(admin.ModelAdmin):
    list_display = ['desire_role']