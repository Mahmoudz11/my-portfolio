from django.urls import path, include

from .views import PortfolioListView, PortfolioDetailView, GeneratePdf

urlpatterns = [
    path('', PortfolioListView.as_view(), name='home'),
    path('<str:slug>', PortfolioDetailView.as_view(), name='pro-detail'),
    path('pdf/', GeneratePdf.as_view(), name='pdf'),

]
