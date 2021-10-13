from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse

# Create your views here.

from .models import Loan

from .serializers import LoanSerializer
"""

class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = '__all__'
"""
class All_Loans(APIView):
    def get(self, request, format=None):
        loans = Loan.objects.all()
        serializer = LoanSerializer(loans, many=True)
        return Response(serializer.data)
