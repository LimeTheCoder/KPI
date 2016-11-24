from __future__ import unicode_literals

from django.db import models

class Person(models.Model):
	name = models.CharField(max_length=50)
	surname = models.CharField(max_length=50)
	middlename = models.CharField(max_length=50, null=True, blank=True)
	birthdate = models.DateField(null=True, blank=True)

	def __str__(self):
		return self.name.encode('utf8') + " " + self.surname.encode('utf8')


class Hospital(models.Model):
	name = models.CharField(max_length=50)
	city = models.CharField(max_length=50)
	state = models.CharField(max_length=50)
	street = models.CharField(max_length=50)
	build_no = models.IntegerField()

	def __str__(self):
		return self.name.encode('utf8')


class Doctor(models.Model):
	person = models.OneToOneField(Person, on_delete=models.CASCADE)
	hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
	position = models.CharField(max_length=50)
	experience = models.IntegerField()

	def __str__(self):
		return self.person.name.encode('utf8') + " " + self.person.surname.encode('utf8')


class SurveyResult(models.Model):
	doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
	pacient = models.ForeignKey(Person, on_delete=models.CASCADE)
	diagnosis = models.CharField(max_length=50, null=True, blank=True)
	closing_date = models.DateField(null=True, blank=True)


class PersonLog(models.Model):
	name = models.CharField(max_length=50)
	surname = models.CharField(max_length=50)
	delete_time = models.DateField()
