from .custom_models import ObjectsManager
from django import forms

class PersonForm(forms.Form):
	id = forms.IntegerField(label = 'id')
	name = forms.CharField(label='Name', max_length = 50)
	surname = forms.CharField(label='Surname', max_length = 50)
	middlename = forms.CharField(label='Middlename', max_length = 50)
	birthdate = forms.DateField(label = 'Birthdate')

class HospitalForm(forms.Form):
	id = forms.IntegerField(label = 'id')
	name = forms.CharField(label='Name', max_length = 50)
	city = forms.CharField(label='City', max_length = 50)
	state = forms.CharField(label='State', max_length = 50)
	street = forms.CharField(label = 'Street', max_length=50)
	build_no = forms.IntegerField(label = 'Build #')


class DoctorForm(forms.Form):
	id = forms.IntegerField(label = 'id')
	person_id = forms.ChoiceField(label='Person', choices = ObjectsManager.get_persons_manager().get_choice_lst)
	hospital_id = forms.ChoiceField(label = 'Hospital', choices = ObjectsManager.get_hospitals_manager().get_choice_lst)
	position = forms.CharField(label='Position', max_length = 50)
	experience = forms.IntegerField(label='Experience')


class SurveyForm(forms.Form):
	id = forms.IntegerField(label = 'id')
	pacient_id = forms.ChoiceField(label='Pacient', choices = ObjectsManager.get_persons_manager().get_choice_lst)
	doctor_id = forms.ChoiceField(label = 'Doctor', choices = ObjectsManager.get_doctors_manager().get_choice_lst)
	diagnosis = forms.CharField(label='Diagnosis', max_length = 50)
	closing_date = forms.DateField(label='Closing Date')