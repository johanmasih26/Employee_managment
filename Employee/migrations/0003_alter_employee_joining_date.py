# Generated by Django 4.0.4 on 2022-05-22 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0002_employee_joining_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='joining_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]