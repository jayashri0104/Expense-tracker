from django.db import models
    

class Expense(models.Model):
      
    CATEGORY_CHOICES = [
        ("household", "Household"),
        ("food", "Food & Groceries"),
        ("transport", "Transportation"),
        ("health", "Health & Personal Care"),
        ("education", "Education"),
        ("entertainment", "Entertainment"),
        ("shopping", "Shopping"),
        ("financial", "Financial"), 
    ]
      
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    title = models.CharField(max_length=200)  
    amount = models.IntegerField()
    quantity = models.IntegerField()
    unit = models.CharField(max_length=50, blank=True)
    paytype = models.CharField( max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)  
    
   
    @property
    def total(self):
        return self.quantity *self.amount