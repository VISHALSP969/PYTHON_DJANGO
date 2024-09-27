from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member

# Create your views here.
def testing(request):
    mydata=Member.objects.all()
    mydata1=Member.objects.all().values()
    mydata2=Member.objects.values_list('firstname')
    template=loader.get_template('template.html')
    context={
        'mymembers':mydata,
        'mymembers1':mydata1,
        'mymembers2':mydata2,
    }
    return HttpResponse(template.render(context,request))