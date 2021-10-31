from django.http import request
from .models import Loan, Loan_Template, Loan_to_Loan_Fund,payments, Ammortization_Table_Row, Ammortization_Table
from rest_framework.response import Response
from .serializers import LoanSerializer,Loan_to_Loan_Fund_Serializer
import numpy as np
import pandas as pd
from django.core import serializers
import json
from rest_framework import status
from .buisness_logic import amortisation_schedule
import json

class myDataFrame:
    interest_rate = 0
    tenor = 0



def get_loans_selector(request):
    print("ZZZZZZZ")
    df_object = myDataFrame()
    loan1 = Loan_to_Loan_Fund.objects.get(loan_col__user= request.user)
    amount= loan1.loan_col.amount
    type= loan1.loan_col.type
    interest_rate= Loan_Template.objects.get(type=type).interest_amount
    #df_object.interest_rate = interest_rate
    tenor= Loan_Template.objects.get(type=type).tenor
    #df.tenor = tenor
    df= amortisation_schedule(amount, interest_rate,tenor,1)
    print(df)
    print(df.shape[0])
    print (df['Instalment'][0])
    pay_instance = payments.objects.create(
       Installment_amount= df['Instalment'][0],
        number_pays= df.shape[0]
    )  
    am_table_instance = Ammortization_Table.objects.create(
        user = request.user 
         
    )  
    for i in range(df.shape[0]):
        row = Ammortization_Table_Row.objects.create(
            am_table = am_table_instance,
            Principal= df['Principal'][i],
            Interest= df['Interest'][i],
            Instalement= df['Instalment'][i],
            Balance=df['Balance'][i]
    )  
    df_json= df.to_json(orient="split")
    response= df_json
    print(response)
    #response = serializers.serialize('json', [loan1], ensure_ascii=False)
    return Response(response, status=status.HTTP_200_OK)

def get_am_table_selector(request):
    print("ZZZZZZZ")
    loan1 = Loan_to_Loan_Fund.objects.get(loan_col__user= request.user)
    
    amount= loan1.loan_col.amount
    type= loan1.loan_col.type
    interest_rate= Loan_Template.objects.get(type=type).interest_amount
    #df_object.interest_rate = interest_rate
    tenor= Loan_Template.objects.get(type=type).tenor
    #df.tenor = tenor
    df= amortisation_schedule(amount, interest_rate,tenor,1)

    pay_instance = payments.objects.create(
       Installment_amount= df['Instalment'][0],
        number_pays= df.shape[0]
    )  
    am_table_instance = Ammortization_Table.objects.create(
        user = request.user 
         
    )  
    for i in range(df.shape[0]):
        row = Ammortization_Table_Row.objects.create(
            am_table = am_table_instance,
            Principal= df['Principal'][i],
            Interest= df['Interest'][i],
            Instalement= df['Instalment'][i],
            Balance=df['Balance'][i]
    )  
    am_table_rows_instance = Ammortization_Table_Row.objects.get(am_table__user = request.user)

    response = serializers.serialize('json', [am_table_rows_instance], ensure_ascii=False)
    return Response(response, status=status.HTTP_200_OK)




