from django.shortcuts import render
from django.http import HttpResponse
from .models import Student

# Create your views here.
def home(request):
    data=Student.objects.all().values()     # fetch all data
    data=Student.objects.filter(id=5)
    Student.objects.filter(id=1).update(name="Vishal")
    data1=Student.objects.filter(id=1)
    Student.objects.filter(id=1).delete()
    data2=Student.objects.all().values()
    return render(request,"home.html",{"data":data,"data1":data1,"data2":data2})
