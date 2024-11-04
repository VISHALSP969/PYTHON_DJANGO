from django.shortcuts import render

# Create your views here.
def book_details(request):
    data={"Type":"Math",
          "list":["Math magic","I Love Mathematics","Mathematics Class 5"]}
    return render(request,"books/bookdetails.html",{"data1":data})