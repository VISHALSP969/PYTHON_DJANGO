from django.shortcuts import render

# Create your views here.
def book_details(request):
    data={}
    # data={"key":"value"}
    return render(request,"books/bookdetails.html",{"data1":data,"mem":"members"})

def members(request):
    data={"title":"django","topic":"templates"}
    return render(request,"books/members.html",{"data1":data,"index":"/"})