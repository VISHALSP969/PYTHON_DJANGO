from django.urls import path
from . import views

urlpatterns=[
    path("np/",views.next_page,name="np"),
]