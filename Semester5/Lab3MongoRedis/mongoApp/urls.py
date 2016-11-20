from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^doctors/$', views.doctor_list, name='doctors'),
    url(r'^surveys/$', views.survey_list, name='surveys'),
    url(r'^doctors/create$', views.doctor_create, name='doctor_create'),
    url(r'^surveys/create$', views.survey_create, name='survey_create'),
    url(r'^doctors/(?P<doctor_id>.+)/$', views.doctor_detail, name='doctor_detail'),
    url(r'^surveys/(?P<survey_id>.+)/$', views.survey_detail, name='survey_detail'),
    url(r'^stats/$', views.stats, name='stats'),
]