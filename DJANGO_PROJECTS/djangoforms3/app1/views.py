from django.shortcuts import render
from .forms import StudentInfo
from .models import Student

# Create your views here.
def home(request):
    if request.method=="POST":
        fm=StudentInfo(request.POST)
        name=request.POST["name"]
        email=request.POST["email"]
        phone=request.POST["phone_no"]
        s=Student(name=name,email=email,phone=phone)
        s.save()
    else:
        fm=StudentInfo(label_suffix="-")
        print(f"get data {fm}")
    return render(request,"home.html",{"form":fm})