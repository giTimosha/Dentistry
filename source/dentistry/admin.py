from django.contrib import admin

from .models import Patient, Card, Employee, Position, Admission_time, Admission

admin.site.register(Patient)
admin.site.register(Card)
admin.site.register(Employee)
admin.site.register(Position)
admin.site.register(Admission_time)
admin.site.register(Admission)