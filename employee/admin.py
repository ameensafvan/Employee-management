from django.contrib import admin
from .models import Employee, Country, JobTitle, UserProfile

# Register your models here.


admin.site.register(Employee)
admin.site.register(Country)
admin.site.register(JobTitle)
admin.site.register(UserProfile)