from django.contrib import admin
from home.models import patient, doctor, organization
# Register your models here.

admin.site.register(patient)
admin.site.register(doctor)
admin.site.register(organization)