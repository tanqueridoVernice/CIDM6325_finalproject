from django.contrib import admin
from django.urls import path, reverse
from django.shortcuts import render
from django import forms
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
# Register your models here.

from WTdegreecheck.models import *

class CsvImportForm(forms.Form):
    csv_upload = forms.FileField()

class WTadmin(admin.ModelAdmin):
    list_display = ('major', 'course', 'is_core', 'is_degree', 'is_major', 'semester', 'year')
    def get_urls(self):
        urls = super().get_urls()
        new_urls = [path('upload-csv/', self.upload_csv),]
        return new_urls + urls
    def upload_csv(self, request):

        if request.method == "POST":
            csv_file = request.FILES["csv_upload"]

            if not csv_file.name.endswith('.csv'):
                messages.warning(request,"wrong file type was uploaded")
                return HttpResponseRedirect(request.path_info)

            file_data = csv_file.read().decode("utf-8")

            csv_data = file_data.split("\n")

            for x in csv_data:
                fields = x.split(",")
                created = Majorcourse.objects.update_or_create(
                    major_id = fields[0],
                    course_id = fields[1],
                    is_core= fields[2],
                    is_degree = fields[3],
                    is_major = fields[4],
                    semester_id = fields[5],
                    year = fields[6]
                )
            url = reverse('admin:index')
            messages.add_message(request, messages.INFO, 'Records successfully added to database')
            return HttpResponseRedirect(url)

        form = CsvImportForm()
        data = {"form": form}
        return render(request, "admin/csv_upload.html", data)





admin.site.register(College)
admin.site.register(Department)
admin.site.register(Semester)
admin.site.register(Degree)
admin.site.register(Major)
admin.site.register(Course)
admin.site.register(Majorcourse, WTadmin)
admin.site.register(Student)
admin.site.register(Studentgrade)
admin.site.register(Faculty)
