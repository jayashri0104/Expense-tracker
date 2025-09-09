from django.contrib import admin
from moneyapp.models import Expense
    
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ['category', 'title', 'amount','quantity','created_at','unit','paytype']
    

admin.site.register(Expense, ExpenseAdmin)

