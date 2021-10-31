from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from djoser.signals import user_activated
# Create your models here.

#class Loan_Type (models.Model):
 #   type=models.CharField(primary_key=True, max_length=1)
class UserProfile(models.Model):  
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance= models.FloatField() 
"""
@receiver(post_save, sender=User)
def create_profile(sender,**kwargs ):
    if kwargs['created']:
        user_profile=UserProfile(user=kwargs['instance'])
        user_profile.save()

post_save.connect(create_profile, sender=User, dispatch_uid="create_profile")
"""
#post_save.connect(create_profile, sender=User)


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
    from_user= models.ForeignKey(User,related_name='loans_set1' ,on_delete=models.CASCADE)
    to_user=models.ForeignKey(User, related_name='loans_set2', on_delete=models.CASCADE)
    amount=models.FloatField()
    


class Loan_to_Loan_Fund(models.Model):
    loan_col = models.ForeignKey(Loan, related_name='loans',on_delete=models.CASCADE)
    loan_fund = models.ForeignKey(Loan, on_delete=models.CASCADE)
    def save(self,*args,**kwargs):
        created = not self.pk
        super().save(*args,**kwargs)
        if created:
            Ledger.objects.create(to_user=self.loan_col.user, from_user=self.loan_fund.user, amount= self.loan_col.amount)
            borrower = UserProfile.objects.get(user=self.loan_col.user)
            lender = UserProfile.objects.get(user=self.loan_fund.user)
            print(self.loan_col.amount)
            borrower.balance = borrower.balance + self.loan_col.amount
            lender.balance = lender.balance - self.loan_fund.amount
            borrower.save()
            lender.save()



"""class payments(models.Model):
    Installment_amount= models.FloatField()
    number_pays= models.IntegerField()



class Ammortization_Table(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    

class Ammortization_Table_Row(models.Model):
    am_table = models.ForeignKey(Ammortization_Table,on_delete=models.CASCADE, null=True, blank=True)
    Principal= models.FloatField()
    Interest= models.FloatField()
    Instalement= models.FloatField()
    Balance=models.FloatField()



class Ammortization_Table_Row(models.Model):
   # am_table = models.ForeignKey(Ammortization_Table,on_delete=models.CASCADE, null=True, blank=True)
    Principals= models.ArrayModelField()
    Interests= models.ListField()
    Instalements= models.ListField()
    Balances=models.ListField()"""


@receiver(user_activated)
def my_handler(user, request, **kwargs):
    user = request.user
    print(request.user.username)
    up = UserProfile.objects.create(user=user, balance=0)
    up.save()