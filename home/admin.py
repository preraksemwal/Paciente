from django.contrib import admin
from home.models import patient, healthcare_professional, organization, booked_appointment
# Register your models here.

admin.site.register(patient)
admin.site.register(healthcare_professional)
admin.site.register(organization)
admin.site.register(booked_appointment)