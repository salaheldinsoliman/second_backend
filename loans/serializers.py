from django.core.serializers import serialize
from django.db.models import fields
from rest_framework import serializers
from django.db import models

from .models import  Loan_Template, Loan, Loan_to_Loan_Fund, Ledger

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
        fields = ['amount', 'to_user', 'from_user']

