from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def next_page(request):
    return HttpResponse("This is second app")