# Generated by Django 3.0.3 on 2020-02-14 22:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Cruise', '0003_auto_20200214_1427'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='excursion',
            options={'ordering': ['id']},
        ),
    ]