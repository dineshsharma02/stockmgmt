from django.shortcuts import render
from .models import Receipt

# Create your views here.
def index(request):
    r_data = Receipt.objects.filter(owner = request.user)
    stocks = {
        "receipt":r_data
    }
    return render(request,'stock/stock_receipt.html')


