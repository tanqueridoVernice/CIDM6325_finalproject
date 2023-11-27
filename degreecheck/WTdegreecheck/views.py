from django.shortcuts import render, get_object_or_404
import csv
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from .models import *
from .forms import MajorForm, MajorTable, Majorcourseform, mctable
import django_tables2 as tables



def welcome_view (request):
    return render(request, 'base.html')

def major_list(request):
    majors = Major.objects.all()
    major_list = []
    for major in majors:
        major_list.append({'major': major})
    context = {'majors':majors}
    return render(request,'major_list.html', context)

def department(request):
    departments = Department.objects.all()
    context = {'departments':departments}
    return render(request,'departments.html', context)
def major(request, pk_test):
    departments = Department.objects.get(id=pk_test)
    majors = departments.major_set.all()
    context = {'departments':departments, 'majors':majors}
    return render(request,'majors.html', context)
def course(request, pk_test):
    majors = Major.objects.get(id=pk_test)
    courses = majors.majorcourse_set.all()
    context = {'majors':majors, 'courses':courses}
    return render(request,'courses.html', context)
def form(request):
    form = MajorForm()
    return render(request, "form.html", {"method": request.method, "form": form})

def mcform(request):
    mcform = Majorcourseform()
    return render(request, "mcform.html", {"method": request.method, "mcform": mcform})

class Majors_table(tables.SingleTableView):
   table_class = MajorTable
   queryset = Major.objects.all()
   template_name = "majors_table.html"

#def mcdata(request):
#    data = Majorcourse.objects.all()
 #   return render(request, 'mctable.html',{'data':data})
class mctable(tables.SingleTableView):
    model = Majorcourse
    table_class = mctable
    template_name = 'mctable.html'

def export(request):
    response = HttpResponse(content_type='text/csv')

    writer = csv.writer(response)
    writer.writerow(['major', 'course', 'is_core', 'is_degree', 'is_major', 'semester', 'year'])

    for x in Majorcourse.objects.all().values_list('major', 'course', 'is_core', 'is_degree', 'is_major', 'semester', 'year'):
        writer.writerow(x)

    response['Content-Disposition'] = 'attachment; filename="major-courses.csv"'

    return response
