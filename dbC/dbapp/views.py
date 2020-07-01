# -*- coding: utf-8 -*-
from django.shortcuts import render
from .models import Emp
from .form import *
from django.http import *

def home(request):
    obj = Emp.objects.all().order_by('age')
    print obj
    return render(request,'index.html',{'obj':obj})
# Create your views here.
def employee1(request):
    if request.method == 'POST':
        form = Emp_form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/employeeform/')
    else:
        form = Emp_form()
    return render(request,'employee_forms.html',{'form':form})
