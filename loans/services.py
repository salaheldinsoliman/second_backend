from .models import Loan, Ledger
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
    


   # user = User.get.objects(user=request.user)
   # user.balance = balance + data['amount']

