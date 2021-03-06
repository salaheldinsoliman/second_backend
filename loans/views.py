from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
import json
from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework import serializers,views
from rest_framework.serializers import Serializer
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.parsers import JSONParser
from django.http import JsonResponse







from django.conf import settings
from django.contrib.auth.models import User
from django.http import Http404


from rest_framework import status, authentication, permissions




# Create your views here.



from .serializers import LoanSerializer, LedgerSerializer
from .services import create_ledger_service, create_loan_service
# create_loan_service, create_ledger_service
from .selector import selectors
from .service import create_ledger,create_loan

import io
from django.http import HttpResponse


@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
class ledger(APIView):
    def get(self, request):
        response=selectors.get_ledger(request)
        return response



@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
class All_Loans(APIView):
    
    def get(self, request, format=None):
        response=selectors.get_loans_selector(request)
        return response




@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])

def loan_create(request):
    tutorial_data = JSONParser().parse(request)
    serializer = LoanSerializer(data=tutorial_data)
    if serializer.is_valid():
        create_loan_service(serializer.validated_data,request)
        #serializer.save(user=request.user)
    return Response(serializer.data)

   

@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def ledger_create(request):
    tutorial_data = JSONParser().parse(request)
    serializer = LedgerSerializer(data=tutorial_data)
    print("before")
    errors = []
    if serializer.is_valid() or 1:
        print("before")
        serializer.errors
        create_ledger_service(serializer.data,request)
        #serializer.save(user=request.user)
    else:
        errors.append({"error": serializer.validated_data})
    print(errors)
    return Response(serializer.data)

   