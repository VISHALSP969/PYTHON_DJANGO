from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def testing(request):
    template=loader.get_template('template.html')
    context={
        'fruits':['Apple','Banana','Cherry','Orange',],
        'cars': [
            {
                'brand': 'Ford',
                'model': 'Mustang',
                'year': '1964',
            },
            {
                'brand': 'Ford',
                'model': 'Bronco',
                'year': '1970',
            },
            {
                'brand': 'Volvo',
                'model': 'P1800',
                'year': '1964',
            }
        ]
    }
    return HttpResponse(template.render(context,request))