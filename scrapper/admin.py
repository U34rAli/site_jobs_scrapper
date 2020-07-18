from django.contrib import admin
from .models import Scrapper, Job, Company


# Register your models here.

class ScrapperAdmin(admin.ModelAdmin):
    list_display = ('scrapper_name', 'added_by', 'how_to_scrap', 'is_active', 'created_at')


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('company', 'name', 'base_url', 'careers_url', 'created_at')


class JobAdmin(admin.ModelAdmin):
    list_display = ('job', 'title', 'description', 'is_active', 'created_at')


admin.site.register(Scrapper, ScrapperAdmin)
admin.site.register(Job, JobAdmin)
admin.site.register(Company, CompanyAdmin)
