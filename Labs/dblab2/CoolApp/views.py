from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .custom_models import ObjectsManager
from .custom_models import Person, Hospital, Doctor
from .forms import PersonForm, HospitalForm, DoctorForm, SurveyForm

def index(request):
	return HttpResponse("Main list")

def doctors_list(request):
	doctors = ObjectsManager.get_doctors_manager().get_all()
	context = { 'objects' : doctors }
	return render(request, 'CoolApp/objects_list.html', context)


def persons_list(request):
	persons = ObjectsManager.get_persons_manager().get_all()
	context = { 'objects' : persons }
	return render(request, 'CoolApp/objects_list.html', context)


def surveys_list(request):
	surveys = ObjectsManager.get_surveys_manager().get_all()
	context = { 'objects' : surveys }
	return render(request, 'CoolApp/objects_list.html', context)


def hospitals_list(request):
	hospitals = ObjectsManager.get_hospitals_manager().get_all()
	context = { 'objects' : hospitals }
	return render(request, 'CoolApp/objects_list.html', context)


def doctor_detail(request, doctor_id):
	if request.method == 'POST':
		if 'delete_btn' in request.POST:
			ObjectsManager.get_doctors_manager().delete_by_id(request.POST["id"])
			return HttpResponseRedirect('/objects/doctors/')
		else:
			form = DoctorForm(request.POST)
			if form.is_valid():
				row = {"person_id" : request.POST["person_id"], "hospital_id" : request.POST["hospital_id"], 
						"position" : request.POST["position"], "experience" : request.POST["experience"]}
				ObjectsManager.get_doctors_manager().update(request.POST["id"], row)
				return HttpResponseRedirect('/objects/doctors/')
	else:
		doctor = ObjectsManager.get_doctors_manager().get_by_id(doctor_id)

		req = {'id' : doctor.id, 'person_id' : doctor.person.id, 'hospital_id' : doctor.hospital.id, 'position' : 
					doctor.position, 'experience' : doctor.experience }
		form = DoctorForm(req)
	context = {'form' : form, 'add_object' : False}
	return render(request, 'CoolApp/object_detail.html', context)


def person_detail(request, person_id):

	if request.method == 'POST':
		if 'delete_btn' in request.POST:
			ObjectsManager.get_persons_manager().delete_by_id(request.POST["id"])
			return HttpResponseRedirect('/objects/persons/')
		else:
			form = PersonForm(request.POST)
			if form.is_valid():
				row = {"name" : request.POST["name"], "surname" : request.POST["surname"], 
						"middlename" : request.POST["middlename"], "birthdate" : request.POST["birthdate"]}
				ObjectsManager.get_persons_manager().update(request.POST["id"], row)
				return HttpResponseRedirect('/objects/persons/')
	else:
		person = ObjectsManager.get_persons_manager().get_by_id(person_id)

		req = {'id' : person.id, 'name' : person.name, 'surname' : person.surname, 'middlename' : 
					person.middlename, 'birthdate' : person.birthdate }
		form = PersonForm(req)
	context = {'form' : form, 'add_object' : False}
	return render(request, 'CoolApp/object_detail.html', context)


def hospital_detail(request, hospital_id):
	
	if request.method == 'POST':
		if 'delete_btn' in request.POST:
			ObjectsManager.get_hospitals_manager().delete_by_id(request.POST["id"])
			return HttpResponseRedirect('/objects/hospitals/')
		else:
			form = HospitalForm(request.POST)
			if form.is_valid():
				row = {"name" : request.POST["name"], "city" : request.POST["city"], 
						"state" : request.POST["state"], "street" : request.POST["street"],
						"build_no" : request.POST["build_no"]}
				ObjectsManager.get_hospitals_manager().update(request.POST["id"], row)
				return HttpResponseRedirect('/objects/hospitals/')
	else:
		hospital = ObjectsManager.get_hospitals_manager().get_by_id(hospital_id)

		req = {'id' : hospital.id, 'name' : hospital.name, 'city' : hospital.city, 'state' : 
					hospital.state, 'street' : hospital.street, 'build_no' : hospital.build_no}
		form = HospitalForm(req)
	context = {'form' : form, 'add_object' : False}
	return render(request, 'CoolApp/object_detail.html', context)



def survey_detail(request, survey_id):
	if request.method == 'POST':
		if 'delete_btn' in request.POST:
			ObjectsManager.get_surveys_manager().delete_by_id(request.POST["id"])
			return HttpResponseRedirect('/objects/surveys/')
		else:
			form = SurveyForm(request.POST)
			if form.is_valid():
				row = {"pacient_id" : request.POST["pacient_id"], "doctor_id" : request.POST["doctor_id"], 
						"diagnosis" : request.POST["diagnosis"], "closing_date" : request.POST["closing_date"]}
				ObjectsManager.get_surveys_manager().update(request.POST["id"], row)
				return HttpResponseRedirect('/objects/surveys/')
	else:
		survey = ObjectsManager.get_surveys_manager().get_by_id(survey_id)

		req = {'id' : survey.id, 'pacient_id' : survey.pacient.id, 'doctor_id' : survey.doctor.id, 'diagnosis' : 
					survey.diagnosis, 'closing_date' : survey.closing_date}
		form = SurveyForm(req)
	context = {'form' : form, 'add_object' : False}
	return render(request, 'CoolApp/object_detail.html', context)


def person_new(request):
	if request.method == 'POST':
		row = {"name" : request.POST["name"], "surname" : request.POST["surname"], 
					"middlename" : request.POST["middlename"], "birthdate" : request.POST["birthdate"]}
		ObjectsManager.get_persons_manager().insert(row)
		return HttpResponseRedirect('/objects/persons/')
	
	form = PersonForm()
	context = {'form' : form, 'add_object' : True}
	return render(request, 'CoolApp/object_detail.html', context)


def hospital_new(request):
	if request.method == 'POST':
		row = {"name" : request.POST["name"], "city" : request.POST["city"], 
						"state" : request.POST["state"], "street" : request.POST["street"],
						"build_no" : request.POST["build_no"]}
		ObjectsManager.get_hospitals_manager().insert(row)
		return HttpResponseRedirect('/objects/hospitals/')
	
	form = HospitalForm()
	context = {'form' : form, 'add_object' : True}
	return render(request, 'CoolApp/object_detail.html', context)


def doctor_new(request):
	if request.method == 'POST':
		row = {"person_id" : request.POST["person_id"], "hospital_id" : request.POST["hospital_id"], 
						"position" : request.POST["position"], "experience" : request.POST["experience"]}
		ObjectsManager.get_doctors_manager().insert(row)
		return HttpResponseRedirect('/objects/doctors/')
	
	form = DoctorForm()
	context = {'form' : form, 'add_object' : True}
	return render(request, 'CoolApp/object_detail.html', context)


def survey_new(request):
	if request.method == 'POST':
		row = {"pacient_id" : request.POST["pacient_id"], "doctor_id" : request.POST["doctor_id"], 
						"diagnosis" : request.POST["diagnosis"], "closing_date" : request.POST["closing_date"]}
		ObjectsManager.get_surveys_manager().insert(row)
		return HttpResponseRedirect('/objects/surveys/')
	
	form = SurveyForm()
	context = {'form' : form, 'add_object' : True}
	return render(request, 'CoolApp/object_detail.html', context)
