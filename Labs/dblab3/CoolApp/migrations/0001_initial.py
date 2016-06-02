# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-05-25 17:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=50)),
                ('experience', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('street', models.CharField(max_length=50)),
                ('build_no', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('middlename', models.CharField(blank=True, max_length=50, null=True)),
                ('birthdate', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SurveyResults',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diagnosis', models.CharField(blank=True, max_length=50, null=True)),
                ('closing_date', models.DateField(blank=True, null=True)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CoolApp.Doctor')),
                ('pacient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CoolApp.Person')),
            ],
        ),
        migrations.AddField(
            model_name='doctor',
            name='hospital',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CoolApp.Hospital'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='person',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='CoolApp.Person'),
        ),
    ]