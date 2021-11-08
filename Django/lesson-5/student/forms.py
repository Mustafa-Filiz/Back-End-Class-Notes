from django import forms
from django.forms import fields
from .models import Student

class StudentForm(forms.ModelForm):
    # first_name = forms.CharField( max_length=50)
    # last_name = forms.CharField( max_length=50)
    # number = forms.IntegerField(required=False)
    class Meta:
        model = Student
        fields = ["first_name", "last_name", "number", "profile_pic"] #="__all__"
        labels = {"first_name": "Name"}