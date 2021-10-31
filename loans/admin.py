from django.contrib import admin

from .models import Ledger, Loan_Template, Loan, UserProfile, Loan_to_Loan_Fund,payments, Ammortization_Table ,Ammortization_Table_Row
# Register your models here.
#admin.site.register(Loan_Type)
admin.site.register(Loan_Template)
admin.site.register(Loan)
admin.site.register(Ledger)
admin.site.register(UserProfile)
admin.site.register(Loan_to_Loan_Fund)
admin.site.register(payments)
admin.site.register(Ammortization_Table)
admin.site.register(Ammortization_Table_Row)


