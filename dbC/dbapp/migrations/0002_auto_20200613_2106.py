# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-06-13 21:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmpContact',
            fields=[
                ('home_id', models.IntegerField(primary_key=True, serialize=False)),
                ('home_add', models.CharField(blank=True, max_length=45, null=True)),
                ('phn', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'emp_contact',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EmpDetail',
            fields=[
                ('detail_id', models.IntegerField(primary_key=True, serialize=False)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, max_length=45, null=True)),
                ('ethencity', models.CharField(blank=True, max_length=45, null=True)),
                ('veteran', models.CharField(blank=True, max_length=45, null=True)),
                ('spouse_f_name', models.CharField(blank=True, max_length=200, null=True)),
                ('spouse_l_name', models.CharField(blank=True, max_length=200, null=True)),
                ('ssn', models.IntegerField(blank=True, db_column='SSN', null=True)),
                ('doj', models.DateField(blank=True, null=True)),
                ('active', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'emp_detail',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EmpFinance',
            fields=[
                ('emp_sal_id', models.IntegerField(primary_key=True, serialize=False)),
                ('emp_salary', models.FloatField(blank=True, null=True)),
                ('hike_salary', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'emp_finance',
                'managed': False,
            },
        ),
        migrations.AlterModelOptions(
            name='emp',
            options={'managed': False},
        ),
    ]
