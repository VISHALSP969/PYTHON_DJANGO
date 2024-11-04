from django.shortcuts import render

# Create your views here.
def book_details(request):
    data=[{
        "title":"Math Magicy",
        "author":"Scott Flansburg"
    },
    {
        "title":"I Love Mathematics",
        "author":"Usha Pandit"
    }]
    return render(request,"books/bookdetails.html",{"data1":data})