# Generated by Django 2.1.2 on 2019-01-19 07:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0006_auto_20190119_0707'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courses',
            name='Number',
        ),
    ]
