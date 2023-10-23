from django import forms
from django.db import models
from .models import Major

class MajorForm(forms.ModelForm):
    class Meta:
        model = Major
        fields = ("__all__")

