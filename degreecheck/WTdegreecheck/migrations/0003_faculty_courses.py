# Generated by Django 4.2 on 2023-11-27 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WTdegreecheck', '0002_faculty'),
    ]

    operations = [
        migrations.AddField(
            model_name='faculty',
            name='courses',
            field=models.ManyToManyField(to='WTdegreecheck.course'),
        ),
    ]
