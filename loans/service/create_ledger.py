
from ..models import Loan, Ledger, UserProfile
from django.contrib.auth.models import User


    
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
    