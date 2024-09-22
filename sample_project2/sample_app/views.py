from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def templateFunction(request):
    template=loader.get_template('sample.html')
    return HttpResponse(template.render())