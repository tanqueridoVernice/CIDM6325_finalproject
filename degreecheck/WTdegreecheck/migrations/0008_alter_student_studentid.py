# Generated by Django 4.2 on 2023-12-02 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WTdegreecheck', '0007_alter_student_adviser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='studentID',
            field=models.CharField(help_text='ex: aa1234567', max_length=100),
        ),
    ]