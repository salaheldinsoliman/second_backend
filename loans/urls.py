from django.urls import path, include
from django.urls.resolvers import URLPattern
from . import views

from .views import All_Loans

urlpatterns = [
    path('all_loans/', views.All_Loans.as_view()),
    #path('Amortization_table/', views.Amortization_table, name="Amortization_table"),
    path('loan_create/', views.loan_create, name="loan_create"),
    path('ledger_create/', views.ledger_create, name="ledger_create"),

    path('ledger/', views.ledger.as_view(), name="ledger"),
#    path('number_view/', views.number_view.as_view(), name="number_view"), 


]
