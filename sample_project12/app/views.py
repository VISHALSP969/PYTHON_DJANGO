from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member

# Create your views here.
def testing(request):
    #Define the list of member data
    member1={'firstname':'Emil','lastname':'Refsnes','phone':5551234,'joined_date':'2022-01-05'}
    member2={'firstname':'Tobias','lastname':'Refsnes','phone':5557777,'joined_date':'2022-04-01'}
    member3={'firstname':'Linus','lastname':'Refsnes','phone':5554321,'joined_date':'2021-12-24'}
    member4={'firstname':'Lene','lastname':'Refsnes','phone':5558888,'joined_date':'2021-05-01'}
    member5={'firstname':'Stalikken','lastname':'Refsnes','phone':5559876,'joined_date':'2022-09-29'}
    
    #List of members
    member_list=[member1,member2,member3,member4,member5]

    #loop through each member and save to the database
    for member_data in member_list:
        #Create a Member obhect
        member=Member(
            firstname=member_data['firstname'],
            lastname=member_data['lastname'],
            phone=member_data['phone'],
            joined_date=member_data['joined_date']
        )
        #save the member object to the database
        # member.save()

    mymembers=Member.objects.all().values()
    template=loader.get_template('template.html')
    context={
        'members':mymembers,
        'emptytestobject':[],
    }
    return HttpResponse(template.render(context,request))