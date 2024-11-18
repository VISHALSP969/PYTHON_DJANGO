from django import forms

class StudentInfo(forms.Form):
    name=forms.CharField(label="First Name")
    email=forms.EmailField(label="Email Address")
    phone_no=forms.IntegerField(label="Phone No")