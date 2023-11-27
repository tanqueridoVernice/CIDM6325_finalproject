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

import WTdegreecheck.views





urlpatterns = [
    path('admin/', admin.site.urls),
    path('', WTdegreecheck.views.welcome_view, name='base,'),
    path('majors/', WTdegreecheck.views.major_list, name='major_list,'),
    path('form/', WTdegreecheck.views.form, name='form,'),
    path('table/', WTdegreecheck.views.Majors_table.as_view(), name='table'),
    path('mcform/', WTdegreecheck.views.mcform, name='mcform'),
    path('data/', WTdegreecheck.views.mctable.as_view(), name='mcdata'),
    path('export/', WTdegreecheck.views.export),
    path('departments/', WTdegreecheck.views.department),
    path('departments/<str:pk_test>', WTdegreecheck.views.major, name = "dept_majors"),
    path('majors/<str:pk_test>', WTdegreecheck.views.course, name = "major_courses"),
]
