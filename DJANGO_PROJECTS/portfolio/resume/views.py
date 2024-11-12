from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.staticfiles.storage import staticfiles_storage

# Create your views here.
def home(request):
    return render(request,"home.html")

def about(request):
    return render(request,"about.html")

def projects(request):
    projects_show=[
        {"title":"Rasoi Connect",
         "path":"images/rasoi_connect.PNG"},
        {"title":"Ecommerse",
         "path":"images/ecommerce.PNG"},
        {"title":"Timetable Scheduler",
         "path":"images/timetable.PNG"},
        {"title":"CRUD",
         "path":"images/CRUD.PNG"},
        {"title":"Phot Uploader",
         "path":"images/photo_uploader.PNG"},
        {"title":"To Do List",
         "path":"images/todolist.PNG"},
        {"title":"Portfolio",
         "path":"images/portfolio.PNG"},
        {"title":"Labour Hiring",
         "path":"images/labour_hiring.PNG"}
    ]
    return render(request,"projects.html",{"projects_show":projects_show})

def experience(request):
    experience=[
        {"company":"Vector India",
         "position":"Embedded Trainee"},
        {"company":"Westen Digital",
         "position":"Firmware Engineer"},
        {"company":"Eduzell Technologies",
         "position":"Web Developer Trainee"}
    ]
    return render(request,"experience.html",{"experience":experience})

def certificate(request):
    return render(request,"certificate.html")

def contact(request):
    return render(request,"contact.html")

def resume(request):
    resume_path="myapp/resume.pdf"
    resume_path=staticfiles_storage.path(resume_path)
    if staticfiles_storage.exists(resume_path):
        with open(resume_path,"rb") as resume_file:
            response=HttpResponse(resume_file.read(),content_type="application/pdf")
            response['Content-Disposition']='attachment';filenmae="resume.pdf"
            return response
    else:
        return HttpResponse("Resume not found",status=404)