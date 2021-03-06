# Generated by Django 2.1.2 on 2019-01-19 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('slug', models.SlugField(max_length=500)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.PositiveIntegerField()),
                ('img', models.ImageField(blank=True, upload_to='profile_pics')),
                ('summery', models.TextField()),
                ('git_hub_link', models.URLField()),
                ('date_of_birth', models.DateField()),
                ('marital_status', models.CharField(max_length=100)),
                ('nationality', models.CharField(max_length=250)),
                ('military_status', models.CharField(max_length=100)),
                ('education', models.CharField(max_length=250)),
                ('certifications', models.CharField(max_length=500)),
                ('courses', models.TextField()),
                ('skills', models.TextField()),
            ],
        ),
    ]
