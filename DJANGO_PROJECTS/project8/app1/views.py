from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request,id):
    # return HttpResponse('<a href="/app2/np">App2</a>')
    return HttpResponse(f"This is Id : {id}")