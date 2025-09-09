from django.urls import path
from .views import Expenseview, Expensecreateview

urlpatterns = [
    path("", Expenseview.as_view(), name="list"),
    path("create/",  Expensecreateview.as_view(), name="create"),
]
