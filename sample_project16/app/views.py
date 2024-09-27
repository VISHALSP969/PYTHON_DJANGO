from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def testing(requsest):
    template=loader.get_template('template.html')
    return HttpResponse(template.render())