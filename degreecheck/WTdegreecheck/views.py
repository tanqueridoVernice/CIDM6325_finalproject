from django.shortcuts import render, get_object_or_404


# Create your views here.

from .models import Major, Core
from .forms import MajorForm

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

def majors_table(request):
    table = MajorForm()
    return render_to_response('majors_table.html', {"method": request.method,"table":table})