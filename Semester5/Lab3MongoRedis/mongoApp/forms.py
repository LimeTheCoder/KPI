from django import forms
from mongo_model import get_doctors_choices, get_symptoms_choices


class DoctorForm(forms.Form):
    name = forms.CharField(label='Name', max_length=50)
    surname = forms.CharField(label='Surname', max_length=50)
    age = forms.IntegerField(label='Age')
    position = forms.CharField(label='Position', max_length = 50)
    experience = forms.IntegerField(label='Experience')


class HospitalForm(forms.Form):
    name = forms.CharField(label='Name', max_length=50)
    city = forms.CharField(label='City', max_length=50)
    state = forms.CharField(label='State', max_length=50)
    street = forms.CharField(label='Street', max_length=50)
    build_no = forms.IntegerField(label='Build #')


class PatientForm(forms.Form):
    name = forms.CharField(label='Name', max_length=50)
    surname = forms.CharField(label='Surname', max_length=50)
    age = forms.IntegerField(label='Age')


class SurveyForm(forms.Form):
    doctor = forms.ChoiceField(label='Doctor', choices=get_doctors_choices)
    diagnosis = forms.CharField(label='Diagnosis', max_length=50)
    open_date = forms.DateTimeField(label='Opening Date')
    is_closed = forms.BooleanField(label='Is closed', required=False, initial=False)
    symptoms = forms.MultipleChoiceField(label='Symptoms', choices=get_symptoms_choices)
