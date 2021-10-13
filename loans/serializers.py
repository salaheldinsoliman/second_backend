from rest_framework import serializers

from .models import Loan_Type, Loan_Template, Loan

class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = '__all__'