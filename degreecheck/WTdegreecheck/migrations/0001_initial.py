# Generated by Django 4.2 on 2023-11-27 05:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='College name', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_ID', models.CharField(help_text='ex. CIDM 6325', max_length=20)),
                ('c_name', models.CharField(help_text='e-commerce and web development', max_length=150)),
                ('hours', models.IntegerField(default=3, help_text='number of credit hours')),
            ],
        ),
        migrations.CreateModel(
            name='Degree',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Degree Name', max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Department name', max_length=100)),
                ('college', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WTdegreecheck.college')),
            ],
        ),
        migrations.CreateModel(
            name='Major',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField()),
                ('name', models.CharField(help_text='Major name', max_length=100)),
                ('college', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='WTdegreecheck.college')),
                ('degree', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WTdegreecheck.degree')),
                ('dept', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='WTdegreecheck.department')),
            ],
        ),
        migrations.CreateModel(
            name='Majorcourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_core', models.BooleanField()),
                ('is_degree', models.BooleanField()),
                ('is_major', models.BooleanField()),
                ('year', models.IntegerField(help_text='program year')),
                ('course', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='WTdegreecheck.course')),
                ('major', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='WTdegreecheck.major')),
            ],
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sem', models.CharField(help_text='Spring,Fall,Summer I, Summer II', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentID', models.CharField(help_text='aa1234567', max_length=100)),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=15)),
                ('major', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='WTdegreecheck.major')),
            ],
        ),
        migrations.CreateModel(
            name='Studentgrade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField()),
                ('grade', models.IntegerField()),
                ('major', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='WTdegreecheck.majorcourse')),
                ('studentID', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='WTdegreecheck.student')),
            ],
        ),
        migrations.AddField(
            model_name='majorcourse',
            name='semester',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='WTdegreecheck.semester'),
        ),
    ]
