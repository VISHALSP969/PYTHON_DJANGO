from django.urls import path
from . import views

urlpatterns=[
    path("",views.book_details,name="bookdetails")
]