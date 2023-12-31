"""degreecheck URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


import WTdegreecheck.views





urlpatterns = [
    path('admin/', admin.site.urls),
    path('', WTdegreecheck.views.welcome_view, name='base,'),
    path('majors/', WTdegreecheck.views.major_list, name='major_list,'),
    path('form/', WTdegreecheck.views.studentform, name='studentform'),
    path('form/upload', WTdegreecheck.views.uploadstudentform, name='uploadstudentform'),
    path('studentpage/', WTdegreecheck.views.studentpage, name='studentpage'),
    path('degreepage/', WTdegreecheck.views.degreepage, name='degreepage'),
    path('table/', WTdegreecheck.views.Majors_table, name='table'),
    path('mcform/', WTdegreecheck.views.mcform, name='mcform'),
    path('data/', WTdegreecheck.views.mctable.as_view(), name='mcdata'),
    path('export/', WTdegreecheck.views.export, name='export'),
    path('exportstudent/', WTdegreecheck.views.exportstudent, name = 'exportstudent'),
    path('departments/', WTdegreecheck.views.department, name='department'),
    path('departments/<str:pk_test>', WTdegreecheck.views.major, name = "dept_majors"),
    path('major/<str:pk_test>', WTdegreecheck.views.course, name = 'course'),
    path('check/<str:pk>', WTdegreecheck.views.coursecheck, name = "coursecheck"),
    path('studentlog/', WTdegreecheck.views.studentlog, name='studentlog'),
    path('studentgrades/<str:pk>', WTdegreecheck.views.studentgrades, name='studentgrades'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)