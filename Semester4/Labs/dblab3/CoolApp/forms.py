from .models import Person, Doctor, Hospital, SurveyResult
from django import forms

class PersonForm(forms.ModelForm):
	class Meta:
		model = Person
		fields = ['name', 'surname', 'middlename', 'birthdate']

class HospitalForm(forms.ModelForm):
	class Meta:
		model = Hospital
		fields = ['name', 'city', 'state', 'street', 'build_no']


class DoctorForm(forms.ModelForm):
	class Meta:
		model = Doctor
		fields = ['person', 'hospital', 'position', 'experience']


class SurveyForm(forms.ModelForm):
	class Meta:
		model = SurveyResult
		fields = ['doctor', 'pacient', 'diagnosis', 'closing_date']