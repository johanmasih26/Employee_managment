# Generated by Django 4.0.4 on 2022-05-22 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='joining_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]