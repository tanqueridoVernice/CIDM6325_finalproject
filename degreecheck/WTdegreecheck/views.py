from django.shortcuts import render, get_object_or_404
import csv
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from .models import Major, Major_course
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
#    data = Major_course.objects.all()
 #   return render(request, 'mctable.html',{'data':data})
class mctable(tables.SingleTableView):
    model = Major_course
    table_class = mctable
    template_name = 'mctable.html'

def export(request):
    response = HttpResponse(content_type='text/csv')

    writer = csv.writer(response)
    writer.writerow(['major', 'course', 'is_core', 'is_degree', 'is_major', 'semester', 'year'])

    for x in Major_course.objects.all().values_list('major', 'course', 'is_core', 'is_degree', 'is_major', 'semester', 'year'):
        writer.writerow(x)

    response['Content-Disposition'] = 'attachment; filename="major-courses.csv"'

    return response
