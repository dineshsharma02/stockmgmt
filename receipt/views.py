from django.shortcuts import redirect, render
from .models import Receipt

# Create your views here.
def index(request):
    if request.method=="GET":
        receipt = Receipt.objects.filter(owner = request.user)
        wheatsum = 0
        ricesum = 0
        combosum = 0
        for i in receipt:
            wheatsum+=i.wheat
            ricesum+=i.rice
            combosum+=i.combo
        context = {
            "receipts":receipt,
            'wheatsum':wheatsum,
            'ricesum':ricesum,
            'combosum':combosum
        }
        return render(request,'receipt/stock_receipt.html',context)
    if request.method=="POST":
        dor = request.POST['date']
        description = request.POST['description']
        wheat = request.POST['wheat']
        rice = request.POST['rice']
        combo = request.POST['combo']
        new_receipt = Receipt.objects.create(owner=request.user,date=dor,description=description,wheat = wheat,rice=rice,combo = combo)
        new_receipt.save()
        return redirect('stock_receipt')


def update_receipt(request,id):
    receipt = Receipt.objects.get(pk=id)
    context = {
        'receipt': receipt
    }
    if request.method=="GET":
        return render(request,"receipt/update_receipt.html",context)

    if request.method=="POST":
        dor = request.POST['date']
        description = request.POST['description']
        wheat = request.POST['wheat']
        rice = request.POST['rice']
        combo = request.POST['combo']
        receipt.owner=request.user
        receipt.date=dor
        receipt.description=description
        receipt.wheat = wheat
        receipt.rice=rice
        receipt.combo = combo
        receipt.save()
    
        return redirect('stock_receipt')
        
def delete_receipt(request, id):
    receipt = Receipt.objects.get(pk=id)
    receipt.delete()
    # messages.success(request, "Expense removed")
    return redirect('stock_receipt')


# def search_dates(request,startdate,enddate):
#     receipt = Receipt.objects.filter(date=)


