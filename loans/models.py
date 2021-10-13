from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class Loan_Type (models.Model):
    type=models.CharField(primary_key=True, max_length=1)
   

class Loan_Template (models.Model):
    amount= models.FloatField()
    type=models.ForeignKey(Loan_Type,on_delete=models.CASCADE)
    min_amount=models.IntegerField()
    max_amount=models.IntegerField()
    tenor=models.IntegerField()

class Loan (models.Model):
    amount= models.FloatField()
    is_loan_fund=models.BooleanField()
    type=models.ForeignKey(Loan_Template, on_delete=models.CASCADE)
    #user = models.ForeignKey()
    is_taken = models.BooleanField() 
