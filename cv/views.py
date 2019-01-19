from django.shortcuts import render
from django.views.generic import ListView, DetailView, View
from django.http import HttpResponse

from .utils import render_to_pdf
from .models import Portfolio, Certifications, Courses, Skills

class PortfolioListView(ListView):
    model = Portfolio
    context_object_name = 'cvs'
    template_name = 'portfolio_list.html'

    def get_context_data(self, **kwargs):
        context = super(PortfolioListView, self).get_context_data(**kwargs)
        context['Certification'] = Certifications.objects.all()
        context['courses'] = Courses.objects.all()
        context['skills'] = Skills.objects.all()
        return context



class PortfolioDetailView(DetailView):
    model = Portfolio

    def get_context_data(self, **kwargs):
        context = super(PortfolioDetailView, self).get_context_data(**kwargs)
        context['Certification'] = Certifications.objects.all()
        context['courses'] = Courses.objects.all()
        context['skills'] = Skills.objects.all()
        return context

class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        pdf = render_to_pdf('pdf/invoice.html', {'cvs':Portfolio.objects.all(),
                                                 'Certification':Certifications.objects.all(),
                                                 'courses':Courses.objects.all(),
                                                 'skills':Skills.objects.all()})
        return pdf
