from django.http import request
from .models import Loan, Loan_Template, Loan_to_Loan_Fund
from rest_framework.response import Response
from .serializers import LoanSerializer
import numpy as np
import pandas as pd

def get_loans_selector(request):
    loans = Loan.objects.all()
    
    serializer = LoanSerializer(loans, many=True)
    return Response(serializer.data)

''''
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
'''

def loans_query():
    instances = Loan_to_Loan_Fund.objects.all()
