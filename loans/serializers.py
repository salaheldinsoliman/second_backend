from django.core.serializers import serialize
from django.db.models import fields
from rest_framework import serializers
from django.db import models

from .models import Ammortization_Table, Loan_Template, Loan, Loan_to_Loan_Fund, Ledger, Ammortization_Table_Row

class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = ['amount','is_taken']


class Loan_to_Loan_Fund_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Loan_to_Loan_Fund
        fields = ['loan']



class LedgerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ledger
        fields = ['amount', 'to_user']



"""class Number(models.Model):
    def __init__(self, likes):
        self.likes = likes

number = Number(likes=10)

class dfSerializer(serializers.ModelSerializer):  
    class Meta:       
        model= Number
        fileds = ['likes']"""



class Ammortization_Table_Row(serializers.ModelSerializer):
    class Meta:
        model = Ammortization_Table_Row
        fields = ['Principal', 'Interest', 'Instalement', 'Balance']
     