from django.contrib import admin

from .models import Portfolio, Certifications, Courses, Skills
admin.site.register(Portfolio)
admin.site.register(Certifications)
admin.site.register(Courses)
admin.site.register(Skills)
