# Generated by Django 3.1.2 on 2020-10-21 08:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Article',
        ),
    ]