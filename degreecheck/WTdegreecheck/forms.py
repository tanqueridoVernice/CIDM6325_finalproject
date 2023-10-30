from django import forms
from django.db import models
from .models import Major, Major_course
import django_tables2 as tables
class MajorForm(forms.ModelForm):
    class Meta:
        model = Major
        fields = ("__all__")

class Majorcourseform(forms.ModelForm):
    class Meta:
        model = Major_course
        fields = ("__all__")

class MajorTable(tables.Table):
    class Meta:
        model = Major

class mctable(tables.Table):
    class Meta:
        model = Major_course