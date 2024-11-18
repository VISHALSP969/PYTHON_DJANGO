from django.shortcuts import render
from .forms import StudentInfo

# Create your views here.
def home(request):
    if request.method=="POST":
        fm=StudentInfo(request.POST)
        print(f"post data {fm}")
    else:
        fm=StudentInfo(label_suffix="-",initial={"name":"First Name","email":"Email"})
        print(f"get data {fm}")
    return render(request,"home.html",{"form":fm})