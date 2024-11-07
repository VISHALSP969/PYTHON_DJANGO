from django.shortcuts import render

# Create your views here.
def book_details(request):
    return render(request,"books/index.html")