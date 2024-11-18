from django import forms

class StudentInfo(forms.Form):
    name=forms.CharField(label="First Name", label_suffix="-",min_length=2,max_length=10,initial="Name",widget=forms.TextInput(attrs={"class":"form-group","id":"form1"}))
    email=forms.EmailField()
    phone_no=forms.IntegerField()