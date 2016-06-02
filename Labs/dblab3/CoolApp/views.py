from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Person, Hospital, Doctor, SurveyResult, PersonLog
from .forms import PersonForm, HospitalForm, DoctorForm, SurveyForm
from django.utils.dateparse import parse_date
from django.db.models import Q
from custom_models import create_person_trigger, drop_trigger, create_event

def index(request):
	return HttpResponse("Main list")

def doctors_list(request):
	msg = False
	if request.method == 'POST' and 'minutes' in request.POST:
		create_event(request.POST['minutes'])
		msg = True

	if 'q' in request.GET and request.GET['q'] != "":
		text = request.GET["q"]
		
		if request.GET.get("optradio", None) == "word":
			query = Q(position__contains=text) | Q(person__name__contains=text) | Q(hospital__name__contains=text) | Q(person__surname__contains=text)
		else:
			query = Q(position__exact=text) | Q(person__name__exact=text) | Q(hospital__name__exact=text) | Q(person__surname__exact=text)
		
		doctors = Doctor.objects.filter(query)
	else:
		doctors = Doctor.objects.all()
	context = { 'objects' : doctors, 'title' : "doctor", 'msg' : msg }
	return render(request, 'CoolApp/objects_list.html', context)


def persons_list(request):
	msg = False
	if request.method == 'POST' and 'minutes' in request.POST:
		create_event(request.POST['minutes'])
		msg = True

	if 'q' in request.GET and request.GET['q'] != "":
		text = request.GET["q"]
		if request.GET.get("optradio", None) == "word":
			query = Q(name__contains=text) | Q(surname__contains=text) | Q(middlename__contains=text)
		else:
			query = Q(name__exact=text) | Q(surname__exact=text) | Q(middlename__exact=text)
		persons = Person.objects.filter(query)
	else:
		persons = Person.objects.all()

	if request.method == 'POST':
		if 'from_date' in request.POST and 'to_date' in request.POST:
			to_date = parse_date(request.POST['to_date'])
			from_date = parse_date(request.POST['from_date'])
			persons = [person for person in persons if person.birthdate >= from_date and person.birthdate <= to_date]
	context = { 'objects' : persons, 'title' : "person", 'msg' : msg }

	return render(request, 'CoolApp/objects_list.html', context)


def surveys_list(request):
	msg = False
	if request.method == 'POST' and 'minutes' in request.POST:
		create_event(request.POST['minutes'])
		msg = True

	if 'q' in request.GET and request.GET['q'] != "":
		text = request.GET["q"]
		if request.GET.get("optradio", None) == "word":
			surveys = SurveyResult.objects.filter(diagnosis__contains=text)
		else:
			surveys = SurveyResult.objects.filter(diagnosis__exact=text)
		
	else:
		surveys = SurveyResult.objects.all()

	if "box" in request.GET:
		surveys = [survey for survey in surveys if survey.closing_date != None]


	context = { 'objects' : surveys, 'title' : "survey", 'msg' : msg }
	return render(request, 'CoolApp/objects_list.html', context)


def hospitals_list(request):
	msg = False
	if request.method == 'POST' and 'minutes' in request.POST:
		create_event(request.POST['minutes'])
		msg = True

	if 'q' in request.GET and request.GET['q'] != "":
		text = request.GET["q"]
		if request.GET.get("optradio", None) == "word":
			query = Q(name__contains=text) | Q(city__contains=text) | Q(street__contains=text)
		else:
			query = Q(name__exact=text) | Q(city__exact=text) | Q(street__exact=text)
		
		hospitals = Hospital.objects.filter(query)
	else:
		hospitals = Hospital.objects.all()

	context = { 'objects' : hospitals, 'title' : "hospital", 'msg' : msg}
	return render(request, 'CoolApp/objects_list.html', context)


def doctor_detail(request, doctor_id):
	if request.method == 'POST':
		if 'delete_btn' in request.POST:
			obj = Doctor.objects.get(id=doctor_id)
			obj.delete()
			return HttpResponseRedirect('/objects/doctors/')
		else:
			row = {"person" : Person.objects.get(id=request.POST["person"]), "hospital" : Hospital.objects.get(id=request.POST["hospital"]), 
					"position" : request.POST["position"], "experience" : request.POST["experience"]}
			Doctor.objects.filter(id=doctor_id).update(**row)
			return HttpResponseRedirect('/objects/doctors/')
	else:
		doctor = Doctor.objects.get(id=doctor_id)
		form = DoctorForm(instance=doctor)
	context = {'form' : form, 'add_object' : False, 'title' : 'doctor'}
	return render(request, 'CoolApp/object_detail.html', context)


def person_detail(request, person_id):

	if request.method == 'POST':
		if 'delete_btn' in request.POST or 'delete_no_log' in request.POST:
			if 'delete_btn' in request.POST:
				create_person_trigger()
			else:
				drop_trigger()
			obj = Person.objects.get(id=person_id)
			obj.delete()
			return HttpResponseRedirect('/objects/persons/')
		else:
			form = PersonForm(request.POST)
			if form.is_valid():
				row = {"name" : request.POST["name"], "surname" : request.POST["surname"], 
						"middlename" : request.POST["middlename"], "birthdate" : request.POST["birthdate"]}
				Person.objects.filter(id=person_id).update(**row)
				return HttpResponseRedirect('/objects/persons/')
	else:
		person = Person.objects.get(id=person_id)
		form = PersonForm(instance=person)

	context = {'form' : form, 'add_object' : False, 'title' : 'person'}
	return render(request, 'CoolApp/object_detail.html', context)


def hospital_detail(request, hospital_id):
	
	if request.method == 'POST':
		if 'delete_btn' in request.POST:
			obj = Hospital.objects.get(id=hospital_id)
			obj.delete()
			return HttpResponseRedirect('/objects/hospitals/')
		else:
			form = HospitalForm(request.POST)
			if form.is_valid():
				row = {"name" : request.POST["name"], "city" : request.POST["city"], 
						"state" : request.POST["state"], "street" : request.POST["street"],
						"build_no" : request.POST["build_no"]}
				SurveyResult.objects.filter(id=hospital_id).update(**row)
				return HttpResponseRedirect('/objects/hospitals/')
	else:
		hospital = Hospital.objects.get(id=hospital_id)
		form = HospitalForm(instance=hospital)

	context = {'form' : form, 'add_object' : False, 'title' : 'hospital'}
	return render(request, 'CoolApp/object_detail.html', context)



def survey_detail(request, survey_id):
	if request.method == 'POST':
		if 'delete_btn' in request.POST:
			obj = SurveyResult.objects.get(id=survey_id)
			obj.delete()
			return HttpResponseRedirect('/objects/surveys/')
		else:
			form = SurveyForm(request.POST)
			if form.is_valid():
				row = {"pacient" : request.POST["pacient"], "doctor" : request.POST["doctor"], 
						"diagnosis" : request.POST["diagnosis"], "closing_date" : request.POST["closing_date"]}
				
				SurveyResult.objects.filter(id=survey_id).update(**row)
				return HttpResponseRedirect('/objects/surveys/')
	else:
		survey = SurveyResult.objects.get(id=survey_id)
		form = SurveyForm(instance=survey)

	context = {'form' : form, 'add_object' : False, 'title' : 'survey'}
	return render(request, 'CoolApp/object_detail.html', context)


def person_new(request):
	if request.method == 'POST':
		row = {"name" : request.POST["name"], "surname" : request.POST["surname"], 
					"middlename" : request.POST["middlename"], "birthdate" : request.POST["birthdate"]}
		
		p = Person(**row)
		p.save()

		return HttpResponseRedirect('/objects/persons/')
	
	form = PersonForm()
	context = {'form' : form, 'add_object' : True}
	return render(request, 'CoolApp/object_detail.html', context)


def hospital_new(request):
	if request.method == 'POST':
		row = {"name" : request.POST["name"], "city" : request.POST["city"], 
						"state" : request.POST["state"], "street" : request.POST["street"],
						"build_no" : request.POST["build_no"]}
		h = Hospital(**row)
		h.save()

		return HttpResponseRedirect('/objects/hospitals/')
	
	form = HospitalForm()
	context = {'form' : form, 'add_object' : True}
	return render(request, 'CoolApp/object_detail.html', context)


def doctor_new(request):
	if request.method == 'POST':
		row = {"person" : Person.objects.get(id=request.POST["person"]), "hospital" : Hospital.objects.get(id=request.POST["hospital"]), 
						"position" : request.POST["position"], "experience" : request.POST["experience"]}
		
		d = Doctor(**row)
		d.save()
		return HttpResponseRedirect('/objects/doctors/')
	
	form = DoctorForm()
	context = {'form' : form, 'add_object' : True}
	return render(request, 'CoolApp/object_detail.html', context)


def survey_new(request):
	if request.method == 'POST':
		row = {"pacient" : Person.objects.get(id=request.POST["pacient"]), "doctor" : Doctor.objects.get(id=request.POST["doctor"]), 
						"diagnosis" : request.POST["diagnosis"], "closing_date" : request.POST["closing_date"]}

		s = SurveyResult(**row)
		s.save()
		return HttpResponseRedirect('/objects/surveys/')
	
	form = SurveyForm()
	context = {'form' : form, 'add_object' : True}
	return render(request, 'CoolApp/object_detail.html', context)

def log(request):
	obj = PersonLog.objects.all()
	context = {'objects' : obj}
	return render(request, 'CoolApp/log.html', context)