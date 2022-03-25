from django.contrib import admin
from jobsapp.models import *

# Register your models here.
class HydJobsAdmin(admin.ModelAdmin):
    list_display = ['date','company','title','eligibility','address','email','phone_no']
admin.site.register(HydJobs,HydJobsAdmin)

class ChennaiJobsAdmin(admin.ModelAdmin):
    list_display = ['date','company','title','eligibility','address','email','phone_no']
admin.site.register(ChennaiJobs,ChennaiJobsAdmin)

class BglrJobsAdmin(admin.ModelAdmin):
    list_display = ['date','company','title','eligibility','address','email','phone_no']
admin.site.register(BglrJobs,BglrJobsAdmin)

class PuneJobsAdmin(admin.ModelAdmin):
    list_display = ['date','company','title','eligibility','address','email','phone_no']
admin.site.register(PuneJobs,PuneJobsAdmin)
