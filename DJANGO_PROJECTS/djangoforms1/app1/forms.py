from django import forms

class StudentInfo(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    phone_no=forms.IntegerField()