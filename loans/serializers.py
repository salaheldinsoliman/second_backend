from rest_framework import serializers

from .models import Loan_Template, Loan

class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = ['amount','is_taken']