from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^doctors/$', views.doctors_list, name='doctors'),
    url(r'^surveys/$', views.surveys_list, name='surveys'),
    url(r'^persons/$', views.persons_list, name='persons'),
    url(r'^hospitals/$', views.hospitals_list, name='hospitals'),

    url(r'^doctors/(?P<doctor_id>[0-9]+)/$', views.doctor_detail, name='doctor_detail'),
    url(r'^persons/(?P<person_id>[0-9]+)/$', views.person_detail, name='person_detail'),
    url(r'^surveys/(?P<survey_id>[0-9]+)/$', views.survey_detail, name='survey_detail'),
    url(r'^hospitals/(?P<hospital_id>[0-9]+)/$', views.hospital_detail, name='hospital_detail'),
    url(r'^persons/new/$', views.person_new, name='person_new'),
    url(r'^hospitals/new/$', views.hospital_new, name='hospital_new'),
    url(r'^doctors/new/$', views.doctor_new, name='doctor_new'),
    url(r'^surveys/new/$', views.survey_new, name='survey_new'),
    url(r'^log', views.log, name='log')
]