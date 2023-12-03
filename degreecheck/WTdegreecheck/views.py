from django.shortcuts import render, get_object_or_404
import csv
from django.shortcuts import render, redirect
from django.http import HttpResponse
from io import BytesIO
from django.template.loader import get_template
from django.views import View
from xhtml2pdf import pisa
# Create your views here.

from .models import *
from .forms import *
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

def coursecheck(request,pk):
    majors = Major.objects.get(id=pk)
    courses = majors.majorcourse_set.all()
    context = {'majors':majors, 'courses':courses}
    return render(request,'coursecheck.html', context)
def studentform(request):
    if request.POST:
        studentform = StudentForm(request.POST)
        if studentform.is_valid():
            studentform.save()
        return redirect(uploadstudentform)

    return render(request, "studentform.html", {"method": request.method, "studentform": StudentForm})

def mcform(request):
    mcform = Majorcourseform()
    return render(request, "mcform.html", {"method": request.method, "mcform": mcform})

def studentpage(request):
    return render(request,"student.html")

def degreepage(request):
    return render(request,"degreepage.html")

def uploadstudentform(request):
    return render(request,"uploadstudentform.html")

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
def exportstudent(request):
    response = HttpResponse(content_type='text/csv')

    writer = csv.writer(response)
    writer.writerow(['studentID', 'firstname', 'lastname', 'phone', 'email', 'major', 'adviser'])

    for x in Student.objects.all().values_list('studentID', 'firstname', 'lastname', 'phone', 'email', 'major', 'adviser'):
        writer.writerow(x)

    response['Content-Disposition'] = 'attachment; filename="students.csv"'

    return response

def render_to_PDF(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")),result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None

class ViewPDF(View):
    def get(self, request, *args, **kwargs):
        pdf = render_to_PDF('majors_table.html')
        return HttpResponse(pdf, content_type='application/pdf')