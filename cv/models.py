from django.db import models
from django.urls import reverse


class Portfolio(models.Model):
    name = models.CharField(max_length=500)
    slug = models.SlugField(max_length=500)
    title = models.CharField(max_length=1000)
    email = models.EmailField()
    phone_number = models.PositiveIntegerField()
    img = models.ImageField(upload_to='profile_pics', blank=True)
    summary = models.TextField()
    git_hub_link = models.URLField(blank=True)
    date_of_birth = models.DateField()
    marital_status = models.CharField(max_length=100)
    nationality = models.CharField(max_length=250)
    military_status = models.CharField(max_length=100)
    education = models.CharField(max_length=250, blank=True)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('cv:pro-detail', args={'pk':self.pk})

class Certifications(models.Model):
    por = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    certifications = models.CharField(max_length=500, blank=True)
    Verify = models.URLField(blank=True)

    def __str__(self):
        return f'{self.por}'

class Courses(models.Model):
    por = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    course_name = models.TextField()

    def __str__(self):
        return f'{self.por}'

class Skills(models.Model):
    por = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    skill = models.CharField(max_length=500)

    def __str__(self):
        return f'{self.por}'
