from django.shortcuts import render

# Create your views here.
def book_details(request):
    data={"math":{"book1":"Math Magicy","book2":"I Love Mathematics"},
          "science":{"book1":"Looking Around: Calss 5","book2":"Science Class 5"}}
    return render(request,"books/bookdetails.html",{"data1":data,"mem":"members"})

def members(request):
    return render(request,"books/members.html",{"index":"/"})