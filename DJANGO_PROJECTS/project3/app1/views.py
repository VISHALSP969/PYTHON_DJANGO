from django.http import HttpResponse

# Create your views here.
def greet(request):
    return HttpResponse("Hi, This is my first project.")

def func2(request):
    return HttpResponse("<h1>This is second function.</h1>")