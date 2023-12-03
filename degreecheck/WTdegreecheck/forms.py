from django import forms
from django.forms import ModelForm
from django.db import models
from .models import *
import django_tables2 as tables
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ("__all__")

class LoginForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ("__all__")

class Majorcourseform(forms.ModelForm):
    class Meta:
        model = Majorcourse
        fields = ("__all__")

class MajorTable(tables.Table):
    class Meta:
        model = Major

class mctable(tables.Table):
    class Meta:
        model = Majorcourse