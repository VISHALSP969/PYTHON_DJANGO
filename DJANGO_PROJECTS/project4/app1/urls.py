from django.urls import path
from . import views

urlpatterns=[
    path('',views.greet,name="index"),
    path('nx/',views.func2,name="nx"),
]