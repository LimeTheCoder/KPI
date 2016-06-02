from django.contrib import admin
from .models import Person, Doctor, Hospital, SurveyResult

# Register your models here.
admin.site.register(Person)
admin.site.register(Hospital)
admin.site.register(Doctor)
admin.site.register(SurveyResult)