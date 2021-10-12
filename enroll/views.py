import json
from django.http.response import JsonResponse
from enroll import models
from django.shortcuts import render
from . import forms
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def home(request):
    form = forms.StuderntRegistration()
    stud = models.User.objects.all()
    context = {
        'form':form,
        'stud':stud
        }
    return render(request, 'base.html', context)

# @csrf_exempt
def savedata(request):
    if request.method == "POST":
        form = forms.StuderntRegistration(request.POST)
        if form.is_valid():
            sid = request.POST.get('stuid')
            name = request.POST['name']
            email = request.POST['email']
            password = request.POST['password']
            if sid == '':
                user = models.User(name=name, email=email, password=password)
            else:
                user = models.User(id=sid, name=name, email=email, password=password)
            user.save()
            stud = models.User.objects.values()
            student_data = list(stud)
            return JsonResponse({'status':'Save', 'student_data':student_data})
        else:
            return JsonResponse({'status':0})

def delete_data(request):
    if request.method == "POST":
        id = request.POST.get('sid')
        pi = models.User.objects.get(pk=id)
        pi.delete()
        return JsonResponse({'status':1})
    else:
        return JsonResponse({'status':0})

def edit_data(request):
    if request.method == 'POST':
        id = request.POST.get('sid')
        student = models.User.objects.get(pk=id)
        student_data ={'id':student.id, 'name':student.name, 'email':student.email, 'password':student.password}
        return JsonResponse(student_data)