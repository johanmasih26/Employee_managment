# Generated by Django 4.0.4 on 2022-05-21 08:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0007_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='movie_title',
            new_name='name',
        ),
    ]