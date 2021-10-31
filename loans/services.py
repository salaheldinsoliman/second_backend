
from .models import Loan, Ledger, UserProfile
from django.contrib.auth.models import User

def create_loan_service(data,request):
    a=''
    print(data['amount']) 
    if (data['amount']<19999):
        a='A'
    if (data['amount']<29999 and data['amount']>20000):
        a='B'
    if (data['amount']<39999 and data['amount']>30000):
         a='C'

    flag = 0
    if (data['is_taken'] == 1):
        flag = 1
    loan= Loan.objects.create(
        amount=data['amount'],
        type=a,
        is_taken=flag,
        user=request.user)
    
def create_ledger_service(data, request):
    print(data['amount'])
    print(data['to_user'])
    user = User.objects.get(username = data['to_user'])
    print("from service")
    ledger = Ledger.objects.create(
        amount = data['amount'],
        to_user = user,
        from_user = request.user
    )    
    to_user = UserProfile.objects.get(user=user)
    to_user.balance = to_user.balance + int(data['amount'])
    to_user.save()

    from_user = UserProfile.objects.get(user=request.user)
    from_user.balance = from_user.balance - int(data['amount'])
    from_user.save()
    