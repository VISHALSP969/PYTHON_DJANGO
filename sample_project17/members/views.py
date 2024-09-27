from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member

# Create your views here.
def testing(request):
    mydata=Member.objects.all()
    mydata1=Member.objects.all().values()
    template=loader.get_template('template.html')
    context={
        'mymembers':mydata,
        'mymembers1':mydata1,
    }
    return HttpResponse(template.render(context,request))