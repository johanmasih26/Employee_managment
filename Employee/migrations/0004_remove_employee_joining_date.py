# Generated by Django 4.0.4 on 2022-05-22 14:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0003_alter_employee_joining_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='joining_date',
        ),
    ]