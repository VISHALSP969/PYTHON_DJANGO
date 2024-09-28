from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member
from django.db.models import Q

# Create your views here.
def testing(request):
    # mydata=Member.objects.filter(firstname="Emil").values()
    # mydata=Member.objects.filter(firstname="Emil",id=1).values()
    # mydata = Member.objects.filter(firstname='Emil').values() | Member.objects.filter(firstname='Tobias').values()
    # mydata = Member.objects.filter(Q(firstname='Emil') | Q(firstname='Lene')).values()
    # Field lookups
    # mydata = Member.objects.filter(firstname__startswith='L').values()
    # mydata = Member.objects.filter(firstname__contains='bias').values()
    # mydata = Member.objects.filter(lastname__icontains='ref').values()
    # mydata = Member.objects.filter(firstname__endswith='s').values()
    # mydata = Member.objects.filter(firstname__exact='Emil').values()
    # mydata = Member.objects.filter(firstname__iexact='emil').values()
    # mydata = Member.objects.filter(firstname__in=['Tobias', 'Linus', 'John']).values()
    # mydata = Member.objects.filter(id__gt=3).values()
    # mydata = Member.objects.filter(id__gte=3).values()
    # mydata = Member.objects.filter(id__lt=3).values()
    # mydata = Member.objects.filter(id__lte=3).values()
    mydata = Member.objects.filter(firstname__istartswith='s').values()
    template=loader.get_template('template.html')
    context={
        'mymembers':mydata,
    }
    return HttpResponse(template.render(context,request))