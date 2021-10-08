from django.shortcuts import redirect, render
from stockoverview.models import Stock
from datetime import date,timedelta
import datetime
import calendar

# Create your views here.
def index(request):
    if request.method=="GET":
        operation='receipt'
        receipt = Stock.objects.filter(owner = request.user,operation=operation).order_by('-date')
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
        operation='receipt'
        dor = request.POST['date']
        description = request.POST['description']
        wheat = request.POST['wheat']
        rice = request.POST['rice']
        combo = request.POST['combo']
        new_receipt = Stock.objects.create(owner=request.user,operation=operation,date=dor,description=description,wheat = wheat,rice=rice,combo = combo)
        new_receipt.save()
        return redirect('stock_receipt')


def update_receipt(request,id):
    operation='receipt'
    receipt = Stock.objects.get(pk=id,operation=operation)
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
        receipt.operation=operation
        receipt.date=dor
        receipt.description=description
        receipt.wheat = wheat
        receipt.rice=rice
        receipt.combo = combo
        receipt.save()
    
        return redirect('stock_receipt')
        
def delete_receipt(request, id):
    operation='receipt'
    receipt = Stock.objects.get(pk=id,operation=operation)
    receipt.delete()
    # messages.success(request, "Expense removed")
    return redirect('stock_receipt')


def search_dates(request):
    if request.method=="POST":
        datef = request.POST['datef']
        datet = request.POST['datet']
        receipt = Stock.objects.filter(owner=request.user,operation = "receipt",date__range=(datef,datet))
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

    if request.method=="GET":
        return redirect('stock_receipt')    

def search_last_seven_days(request):
    datef = date.today()- timedelta(7)
    datet = date.today()
    receipt = Stock.objects.filter(owner=request.user,operation = "receipt",date__range=(datef,datet))
    
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


def search_last_month(request):

    last_day_of_prev_month = date.today().replace(day=1) - timedelta(days=1)
    start_day_of_prev_month = date.today().replace(day=1) - timedelta(days=last_day_of_prev_month.day)
    datef = start_day_of_prev_month
    datet = last_day_of_prev_month
    receipt = Stock.objects.filter(owner=request.user,operation = "receipt",date__range=(datef,datet))
    
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

    
def search_this_month(request):
    today = date.today()
    start_day_of_this_month = date.today().replace(day=1)
    last_day_num = calendar.monthrange(today.year,today.month)[1]
    last_day_of_this_month = today.replace(day=last_day_num)

    datef = start_day_of_this_month
    datet = last_day_of_this_month
    receipt = Stock.objects.filter(owner=request.user,operation = "receipt",date__range=(datef,datet))
    
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
 

def search_this_year(request):
    startday = date(date.today().year, 1, 1)
    endday = date(date.today().year, 12, 31)

    
    
    datef = startday
    datet = endday
    receipt = Stock.objects.filter(owner=request.user,operation = "receipt",date__range=(datef,datet))
    
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
