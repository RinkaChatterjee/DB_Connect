# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class Emp(models.Model):
    fname = models.CharField(db_column='Fname', max_length=45)  # Field name made lowercase.
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    lname = models.CharField(db_column='Lname', max_length=45)  # Field name made lowercase.
    age = models.IntegerField(db_column='Age')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'emp'


class EmpContact(models.Model):
    home_id = models.IntegerField(primary_key=True)
    home_add = models.CharField(max_length=45, blank=True, null=True)
    phn = models.IntegerField(blank=True, null=True)
    detail = models.ForeignKey('EmpDetail', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'emp_contact'


class EmpDetail(models.Model):
    detail_id = models.IntegerField(primary_key=True)
    age = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=45, blank=True, null=True)
    ethencity = models.CharField(max_length=45, blank=True, null=True)
    veteran = models.CharField(max_length=45, blank=True, null=True)
    spouse_f_name = models.CharField(max_length=200, blank=True, null=True)
    spouse_l_name = models.CharField(max_length=200, blank=True, null=True)
    ssn = models.IntegerField(db_column='SSN', blank=True, null=True)  # Field name made lowercase.
    doj = models.DateField(blank=True, null=True)
    active = models.CharField(max_length=45, blank=True, null=True)
    id = models.ForeignKey(Emp, models.DO_NOTHING, db_column='id', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'emp_detail'


class EmpFinance(models.Model):
    emp_sal_id = models.IntegerField(primary_key=True)
    emp_salary = models.FloatField(blank=True, null=True)
    hike_salary = models.FloatField(blank=True, null=True)
    detail = models.ForeignKey(EmpDetail, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'emp_finance'

# Create your models here.
