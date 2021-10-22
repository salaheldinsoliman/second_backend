from django.http import request
from .models import Loan, Loan_Template, Loan_to_Loan_Fund
from rest_framework.response import Response
from .serializers import LoanSerializer,Loan_to_Loan_Fund_Serializer
import numpy as np
import pandas as pd
from django.core import serializers
import json
from rest_framework import status
def get_loans_selector(request):
    
    loan1 = Loan_to_Loan_Fund.objects.get(loan__user= request.user)
    print(loan1.loan.amount)
    #loans = Loan.objects.filter(user=request.user)
    amount= loan1.loan.amount
    type= loan1.loan.type
    print(type)
    interest_rate= Loan_Template.objects.get(type=type).interest_amount
    print(interest_rate)
    tenor= Loan_Template.objects.get(type=type).tenor
    print(tenor)
    df= amortisation_schedule(amount, interest_rate,tenor,1)
    print(df)
    #serializer = Loan_to_Loan_Fund_Serializer(loan1, many=True)
    #return Response(serializer.data)
    response = serializers.serialize('json', [loan1], ensure_ascii=False)
    return Response(response, status=status.HTTP_200_OK)


def PMT(rate, nper,pv, fv=0, type=0):
    if rate!=0:
               pmt = (rate*(fv+pv*(1+ rate)**nper))/((1+rate*type)*(1-(1+ rate)**nper))
    else:
               pmt = (-1*(fv+pv)/nper)  
    return(pmt)


def IPMT(rate, per, nper,pv, fv=0, type=0):
  ipmt = -( ((1+rate)**(per-1)) * (pv*rate + PMT(rate, nper,pv, fv=0, type=0)) - PMT(rate, nper,pv, fv=0, type=0))
  return(ipmt)


def PPMT(rate, per, nper,pv, fv=0, type=0):
  ppmt = PMT(rate, nper,pv, fv=0, type=0) - IPMT(rate, per, nper, pv, fv=0, type=0)
  return(ppmt)

def amortisation_schedule(amount, annualinterestrate, paymentsperyear, years):

    df = pd.DataFrame({'Principal' :[PPMT(annualinterestrate/paymentsperyear, i+1, paymentsperyear*years, amount) for i in range(paymentsperyear*years)],
                                 'Interest' :[IPMT(annualinterestrate/paymentsperyear, i+1, paymentsperyear*years, amount) for i in range(paymentsperyear*years)]})
    
    df['Instalment'] = df.Principal + df.Interest
    df['Balance'] = amount + np.cumsum(df.Principal)
    return(df)


def loans_query():
    loan1 = Loan_to_Loan_Fund.objects.get(loan__user= request.user)
    amount= loan1.loan.amount
    type= loan1.loan.type
    interest_rate= Loan_Template.objects.get(type=type).interest_amount
    tenor= Loan_Template.objects.get(type=type).tenor
    df= amortisation_schedule(amount,interest_rate,tenor,1)
    df

