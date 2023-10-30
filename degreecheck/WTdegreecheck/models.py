from django.db import models

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


class Major_course(models.Model):
    major = models.ForeignKey(Major,on_delete=models.CASCADE, default=0)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, default=0)
    is_core = models.BooleanField()
    is_degree = models.BooleanField()
    is_major = models.BooleanField()
    semester = models.ForeignKey(Semester,on_delete=models.CASCADE, default=0)
    year = models.IntegerField(help_text="program year")


