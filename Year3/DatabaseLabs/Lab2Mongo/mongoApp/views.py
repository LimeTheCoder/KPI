from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages

from mongo_model import *
from forms import *
from pymongo.database import DBRef


def stats(request):
    return render(request, 'mongoApp/stats.html', {'lst' : get_disease_stats(),
                                                   'hospitals' : get_hospital_personal_cnt(),
                                                   'positions' : get_position_cnt()})


def doctor_list(request):
    page = 1
    if request.method == 'POST':
        print request.POST
        page = int(request.POST['page'])
        if 'prev' in request.POST:
            page -= 1
        if 'next' in request.POST:
            page += 1
    doctors, has_prev, has_next = get_doctor_list(page)
    context = {'doctors': doctors, 'page' : page,
               'has_prev' : has_prev, 'has_next' : has_next}
    return render(request, 'mongoApp/doctor_list.html', context)


def survey_list(request):
    context = {}

    if request.method == 'POST':
        surveys = find_surveys(request.POST['search'])
        if surveys:
            messages.add_message(request, messages.SUCCESS,
                             'Search by request "' + request.POST['search'] + '" performed successfully')
        else:
            context['error'] = "Didn't find anything by your request '" + request.POST['search'] + "'"
            surveys = get_survey_list()
    else:
        surveys = get_survey_list()

    context['surveys'] = surveys
    return render(request, 'mongoApp/survey_list.html', context)


def doctor_detail(request, doctor_id):
    error = None

    if request.method == 'POST':
        if 'delete_btn' in request.POST:
            delete_doctor(doctor_id)
            messages.add_message(request, messages.SUCCESS, 'Doctor object deleted successfully')
            return HttpResponseRedirect('/objects/doctors/')

        doctor_form = DoctorForm(request.POST, prefix='doctor')
        hospital_form = HospitalForm(request.POST, prefix='hospital')

        if doctor_form.is_valid() and hospital_form.is_valid():
            data = doctor_form.cleaned_data
            data['hospital'] = hospital_form.cleaned_data

            doctor = Doctor(data)
            update_doctor(doctor_id, doctor)
            messages.add_message(request, messages.SUCCESS, 'Doctor object updated successfully')
            return HttpResponseRedirect('/objects/doctors/')

        error = "Please fill all fields correctly"

    dict = get_doctor_by_id(doctor_id).to_dict()
    hospital_dict = dict['hospital']

    for key in dict.keys():
        dict['doctor-' + key] = dict.pop(key)

    for key in hospital_dict.keys():
        hospital_dict['hospital-' + key] = hospital_dict.pop(key)

    context = {'doctor_form': DoctorForm(dict, prefix='doctor'), 'edit_mode' : True,
               'hospital_form': HospitalForm(hospital_dict, prefix='hospital')}
    if error is not None: context['error'] = error

    return render(request, 'mongoApp/doctor_detail.html', context)


def doctor_create(request):
    error = None

    if request.method == 'POST':
        doctor_form = DoctorForm(request.POST, prefix='doctor')
        hospital_form = HospitalForm(request.POST, prefix='hospital')

        if doctor_form.is_valid() and hospital_form.is_valid():
            data = doctor_form.cleaned_data
            data['hospital'] = hospital_form.cleaned_data

            doctor = Doctor(data)
            insert_doctor(doctor)
            messages.add_message(request, messages.SUCCESS, 'Doctor object created successfully')
            return HttpResponseRedirect('/objects/doctors/')

        error = "Please fill all fields correctly"

    context = {'doctor_form': DoctorForm(prefix='doctor'), 'hospital_form': HospitalForm(prefix='hospital')}
    if error is not None: context['error'] = error

    return render(request, 'mongoApp/doctor_detail.html', context)


def survey_create(request):
    error = None

    if request.method == 'POST':
        survey_form = SurveyForm(request.POST, prefix='survey')
        patient_form = PatientForm(request.POST, prefix='patient')

        if survey_form.is_valid() and patient_form.is_valid():
            data = survey_form.cleaned_data
            data['pacient'] = patient_form.cleaned_data
            data['doctor_ref']= DBRef('doctors', data['doctor'])
            survey = Survey(data)
            insert_survey(survey)
            messages.add_message(request, messages.SUCCESS, 'Survey object created successfully')
            return HttpResponseRedirect('/objects/surveys/')

        error = "Please fill all fields correctly"

    context = {'survey_form': SurveyForm(prefix='survey'), 'patient_form': PatientForm(prefix='patient')}
    if error is not None: context['error'] = error

    return render(request, 'mongoApp/survey_detail.html', context)


def survey_detail(request, survey_id):
    error = None

    if request.method == 'POST':
        if 'delete_btn' in request.POST:
            delete_survey(survey_id)
            messages.add_message(request, messages.SUCCESS, 'Survey object deleted successfully')
            return HttpResponseRedirect('/objects/surveys/')

        survey_form = SurveyForm(request.POST, prefix='survey')
        patient_form = PatientForm(request.POST, prefix='patient')

        if survey_form.is_valid() and patient_form.is_valid():
            data = survey_form.cleaned_data
            data['pacient'] = patient_form.cleaned_data
            data['doctor_ref'] = DBRef('doctors', data['doctor'])

            survey = Survey(data)
            update_survey(survey_id, survey)

            messages.add_message(request, messages.SUCCESS, 'Survey object updated successfully')
            return HttpResponseRedirect('/objects/surveys/')

        error = "Please fill all fields correctly"

    dict = get_survey_by_id(survey_id).to_dict()
    dict['doctor'] = dict['doctor_ref'].id
    patient_dict = dict['pacient']

    for key in dict.keys():
        dict['survey-' + key] = dict.pop(key)

    for key in patient_dict.keys():
        patient_dict['patient-' + key] = patient_dict.pop(key)

    context = {'survey_form': SurveyForm(dict, prefix='survey'), 'edit_mode' : True,
               'patient_form': PatientForm(patient_dict, prefix='patient')}
    if error is not None: context['error'] = error

    return render(request, 'mongoApp/survey_detail.html', context)