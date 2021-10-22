from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User

# Create your models here.

#class Loan_Type (models.Model):
 #   type=models.CharField(primary_key=True, max_length=1)
class UserProfile(models.Model):  
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance= models.FloatField()  
    #other fields s


class Loan_Template (models.Model):
    interest_amount= models.FloatField()
    type=models.CharField(primary_key=True, max_length=1)
    min_amount=models.IntegerField()
    max_amount=models.IntegerField()
    tenor=models.IntegerField()

class Loan (models.Model):
    #id = models.PositiveIntegerField(primary_key=True)
    amount= models.FloatField()
    is_loan_fund=models.BooleanField(default=False)
    type=models.CharField(max_length=1)
    user = models.ForeignKey(User,related_name='loans',on_delete=models.CASCADE)
    is_taken = models.BooleanField(default=False)
    pmt= models.FloatField(default=0)

    def __str__(self):
        return str(self.user.username)


class Ledger(models.Model):
    from_user= models.ForeignKey(UserProfile,related_name='loans' ,on_delete=models.CASCADE)
    to_user=models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    amount=models.FloatField()
    


class Loan_to_Loan_Fund(models.Model):
    loan = models.ForeignKey(Loan, related_name='loans',on_delete=models.CASCADE)
    loan_fund = models.ForeignKey(Loan, on_delete=models.CASCADE)
