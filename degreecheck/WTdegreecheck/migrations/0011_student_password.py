# Generated by Django 4.2.6 on 2023-12-03 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WTdegreecheck', '0010_alter_student_options_alter_student_managers_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='password',
            field=models.CharField(default=123456, max_length=100),
            preserve_default=False,
        ),
    ]