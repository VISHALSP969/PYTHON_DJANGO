from django.shortcuts import render

# Create your views here.
def home(request):
    context={"username":"John Doe"}
    return render(request,"App/home.html",context)