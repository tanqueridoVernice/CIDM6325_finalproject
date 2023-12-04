import django_filters
from .models import *

class MajorFilterSet(django_filters.FilterSet):
    class Meta:
        model = Major
        fields = '__all__'

class StudentFilterSet(django_filters.FilterSet):
    class Meta:
        model = Studentgrade
        fields = ['studentID']