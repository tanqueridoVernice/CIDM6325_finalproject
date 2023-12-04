from django import forms
from django.forms import ModelForm
from django.db import models
from .models import *
import django_tables2 as tables
from django_tables2.utils import A
from django.urls import reverse

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

class Studentlog(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['studentID', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }

class MajorTable(tables.Table):
    view_link = tables.LinkColumn('course', args=[A('pk')], text='View Courses')
    class Meta:
        model = Major
        

class mctable(tables.Table):
    class Meta:
        model = Majorcourse

class Studentgrades(tables.Table):
    class Meta:
        model = Studentgrade