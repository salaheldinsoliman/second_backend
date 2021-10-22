from rest_framework import serializers

from .models import Loan_Template, Loan, Loan_to_Loan_Fund

class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = ['amount','is_taken']


class Loan_to_Loan_Fund_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Loan_to_Loan_Fund
        fields = ['loan']