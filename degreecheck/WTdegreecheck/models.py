from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class College(models.Model):
    name = models.CharField(max_length=100, help_text="College name")

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=100, help_text="Department name")
    college = models.ForeignKey(College, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Semester(models.Model):
    sem = models.CharField(max_length=50,help_text="Spring,Fall,Summer I, Summer II")
    def __str__(self):
        return self.sem


class Course(models.Model):
    c_ID = models.CharField(max_length=20, help_text="ex. CIDM 6325")
    c_name = models.CharField(max_length= 150, help_text="e-commerce and web development")
    hours = models.IntegerField(default=3,help_text="number of credit hours")
    def __str__(self):
        return self.c_name

class Degree(models.Model):
    name = models.CharField(max_length=150, help_text="Degree Name")

    def __str__(self):
        return self.name
class Major(models.Model):
    code = models.IntegerField()
    degree = models.ForeignKey(Degree, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, help_text="Major name")
    college = models.ForeignKey(College,on_delete=models.CASCADE, default=0)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE, default = 0)

    def __str__(self):
        return self.name


class Majorcourse(models.Model):
    major = models.ForeignKey(Major,on_delete=models.CASCADE, default=0)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, default=0)
    is_core = models.BooleanField()
    is_degree = models.BooleanField()
    is_major = models.BooleanField()
    semester = models.ForeignKey(Semester,on_delete=models.CASCADE, default=0)
    year = models.IntegerField(help_text="program year")
    def __str__(self):
        return self.course.c_ID
class Faculty(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField
    department = models.ForeignKey(Department, on_delete=models.CASCADE, default = 0)
    courses = models.ManyToManyField(Course)
    def __str__(self):
        return f'{self.firstname} {self.lastname}'
class Student(models.Model):
    studentID = models.CharField(max_length=100, help_text="ex: aa1234567")
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=250, null=True)
    major = models.ForeignKey(Major,on_delete=models.CASCADE, default=0)
    adviser = models.ForeignKey(Faculty,on_delete=models.CASCADE, default=0, null=True)
    def __str__(self):
        return self.studentID


class Studentgrade(models.Model):
    studentID = models.ForeignKey(Student,on_delete=models.CASCADE, default=0)
    course = models.ForeignKey(Majorcourse,on_delete=models.CASCADE, default=0)
    status = models.BooleanField()
    grade = models.IntegerField()
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE, default=0)
    yeartaken = models.IntegerField(help_text="program year")



