from django.urls import path, include
from django.urls.resolvers import URLPattern
from . import views

from .views import All_Loans

urlpatterns = [
    path('all_loans/', views.All_Loans.as_view()),
    path('loan_create/', views.loan_create, name="loan_create")


]
