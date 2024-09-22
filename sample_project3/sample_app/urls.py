from django.urls import path
from . import views

urlpatterns=[
    path("template/",views.sampleFunction,name='template')
]