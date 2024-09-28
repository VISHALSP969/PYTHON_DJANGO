from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member

# Create your views here.
def testing(request):
    mydata=Member.objects.filter(firstname="Emil").values()
    template=loader.get_template('template.html')
    context={
        'mymembers':mydata,
    }
    return HttpResponse(template.render(context,request))