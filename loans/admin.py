from django.contrib import admin
from .models import Loan_Type, Loan_Template, Loan
# Register your models here.
admin.site.register(Loan_Type)
admin.site.register(Loan_Template)
admin.site.register(Loan)


