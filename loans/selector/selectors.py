from django.http import request
from ..models import Ledger, Loan, Loan_Template, Loan_to_Loan_Fund
from rest_framework.response import Response
from ..serializers import LoanSerializer,Loan_to_Loan_Fund_Serializer
import numpy as np
import pandas as pd
from django.core import serializers
import json
from rest_framework import status
from ..buisness_logic import amortisation_schedule
import json



def get_loans_selector(request):
    loan1 = Loan_to_Loan_Fund.objects.get(loan_col__user= request.user)
    amount= loan1.loan_col.amount
    type= loan1.loan_col.type
    interest_rate= Loan_Template.objects.get(type=type).interest_amount
    #df_object.interest_rate = interest_rate
    tenor= Loan_Template.objects.get(type=type).tenor
    #df.tenor = tenor
    df= amortisation_schedule(amount, interest_rate,tenor,1)
    df_json= df.to_json(orient="split")
    response= df_json
    print(response)
    #response = serializers.serialize('json', [loan1], ensure_ascii=False)
    return Response(response, status=status.HTTP_200_OK)

def get_ledger(request):
    ledger_objects_to = Ledger.objects.get(to_user=request.user)
    ledger_objects_from = Ledger.objects.get(from_user=request.user)
    all_ledger_objects = ledger_objects_to | ledger_objects_from
    response = serializers.serialize('json', [all_ledger_objects], ensure_ascii=False)
    return Response(response, status=status.HTTP_200_OK)
