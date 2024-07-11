from django.shortcuts import render,HttpResponse
import json
from .models import Employee,Role,Department
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
# Create your views here.
def index(request):
    return render(request, 'index.html')

def all_emp(request):
    emps = Employee.objects.all()
    context ={
            'emps': emps
            }
    print(context)
    return render(request, 'all_emp.html',context)
@csrf_exempt
def add_emp(request):
    if request.method =='POST':
        req=(json.loads(request.body.decode("UTF-8")))
        first_name = req['first_name']
        last_name = req['last_name']
        salary = req['salary']
        bonus = req['bonus']
        phone = req['phone']
        dept = req['dept']
        role = req['role']
        new_emp = Employee(first_name= first_name,last_name = last_name,salary= salary,bonus= bonus ,phone= phone,dept_id= dept,role_id= role,hire_date= datetime.now())
        new_emp.save()
        return HttpResponse('new employee')
    elif request.method=='GET':
        return render(request, 'add_emp.html')
    else:
        return HttpResponse('error')


def remove_emp(request,emp_id = 0):
    if emp_id:
        try:
            emp_to_be_removed =Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return HttpResponse("Employee removed")
        except:
            return HttpResponse("enter a valid emp id")
    emps = Employee.objects.all()
    context ={
            'emps' : emps
            }
    return render(request, 'remove_emp.html',context)

def filter_emp(request):
    if request.method == 'POST':
        name = request.POST['name']
        dept = request.POST['dept']
        role = request.POST['role']
        emps =Employee.objects.all()
        if name:
            emps = emps.filter(Q(first_name__icontains = name) | Q(last_name__icontains = name))
        if dept:
            emps = emps.filter(dept__name__icontains = dept)
        if role:
            emps = emps.filter(role__name__icontains = role)

        context = {
            'emps' : emps
        }      
        return render(request, 'all_emp.html',context)

    elif request.method == 'GET':
        return render(request,'filter_emp.html')
    else:
        return HttpResponse('error')

