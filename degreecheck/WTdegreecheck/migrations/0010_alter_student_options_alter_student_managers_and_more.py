# Generated by Django 4.2 on 2023-12-02 23:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WTdegreecheck', '0009_alter_student_options_alter_student_managers_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={},
        ),
        migrations.AlterModelManagers(
            name='student',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='student',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='student',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='student',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='student',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='student',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='student',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='student',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='student',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='student',
            name='password',
        ),
        migrations.RemoveField(
            model_name='student',
            name='user_permissions',
        ),
        migrations.RemoveField(
            model_name='student',
            name='username',
        ),
    ]
