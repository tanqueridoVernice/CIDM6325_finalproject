from django import forms
from django.db import models
from .models import Major
import django_tables2 as tables
class MajorForm(forms.ModelForm):
    class Meta:
        model = Major
        fields = ("__all__")

class MajorTable(tables.Table):
    class Meta:
        model = Major

