from django.shortcuts import redirect, render
from stockoverview.models import Stock
from datetime import date,timedelta
import datetime
import calendar

# Create your views here.
def index(request):
    if request.method=="GET":
        exp = Stock.objects.filter(owner = request.user,operation='consumption')
        wheatsum = 0
        ricesum = 0
        combosum = 0
        for i in exp:
            wheatsum+=i.wheat
            ricesum+=i.rice
            combosum+=i.combo
        context = {
            "exps":exp,
            'wheatsum':wheatsum,
            'ricesum':ricesum,
            'combosum':combosum
        }
        return render(request,'consumption/stock_exp.html',context)
    if request.method=="POST":
        dor = request.POST['date']
        description = request.POST['description']
        wheat = request.POST['wheat']
        rice = request.POST['rice']
        combo = request.POST['combo']
        operation='consumption'
        new_exp = Stock.objects.create(owner=request.user,operation=operation,date=dor,description=description,wheat = wheat,rice=rice,combo = combo)
        new_exp.save()
        return redirect('stock_exp')


def update_exp(request,id):
    operation='consumption'
    exp = Stock.objects.get(pk=id,operation=operation)
    context = {
        'exp': exp
    }
    if request.method=="GET":
        return render(request,"consumption/update_exp.html",context)

    if request.method=="POST":
        dor = request.POST['date']
        description = request.POST['description']
        wheat = request.POST['wheat']
        rice = request.POST['rice']
        combo = request.POST['combo']
        exp.owner=request.user
        exp.operation=operation
        exp.date=dor
        exp.description=description
        exp.wheat = wheat
        exp.rice=rice
        exp.combo = combo
        exp.save()
    
        return redirect('stock_exp')
        
def delete_exp(request, id):
    operation='consumption'
    exp = Stock.objects.get(pk=id,operation=operation)
    exp.delete()
    # messages.success(request, "Expense removed")
    return redirect('stock_exp')


def search_dates(request):
    if request.method=="POST":
        datef = request.POST['datef']
        datet = request.POST['datet']
        exp = Stock.objects.filter(owner=request.user,operation = "consumption",date__range=(datef,datet))
        wheatsum = 0
        ricesum = 0
        combosum = 0
        for i in exp:
            wheatsum+=i.wheat
            ricesum+=i.rice
            combosum+=i.combo
        context = {
            "exps":exp,
            'wheatsum':wheatsum,
            'ricesum':ricesum,
            'combosum':combosum
        }
        
        return render(request,'consumption/stock_exp.html',context)

    if request.method=="GET":
        return redirect('stock_exp')    

def search_last_seven_days(request):
    datef = date.today()- timedelta(7)
    datet = date.today()
    exp = Stock.objects.filter(owner=request.user,operation = "consumption",date__range=(datef,datet))
    
    wheatsum = 0
    ricesum = 0
    combosum = 0
    for i in exp:
        wheatsum+=i.wheat
        ricesum+=i.rice
        combosum+=i.combo
    context = {
        "exps":exp,
        'wheatsum':wheatsum,
        'ricesum':ricesum,
        'combosum':combosum
    }
    return render(request,'consumption/stock_exp.html',context)


def search_last_month(request):

    last_day_of_prev_month = date.today().replace(day=1) - timedelta(days=1)
    start_day_of_prev_month = date.today().replace(day=1) - timedelta(days=last_day_of_prev_month.day)
    datef = start_day_of_prev_month
    datet = last_day_of_prev_month
    exp = Stock.objects.filter(owner=request.user,operation = "consumption",date__range=(datef,datet))
    
    wheatsum = 0
    ricesum = 0
    combosum = 0
    for i in exp:
        wheatsum+=i.wheat
        ricesum+=i.rice
        combosum+=i.combo
    context = {
        "exps":exp,
        'wheatsum':wheatsum,
        'ricesum':ricesum,
        'combosum':combosum
    }
    
    return render(request,'consumption/stock_exp.html',context)    

    
def search_this_month(request):
    today = date.today()
    start_day_of_this_month = date.today().replace(day=1)
    last_day_num = calendar.monthrange(today.year,today.month)[1]
    last_day_of_this_month = today.replace(day=last_day_num)

    datef = start_day_of_this_month
    datet = last_day_of_this_month
    exp = Stock.objects.filter(owner=request.user,operation = "consumption",date__range=(datef,datet))
    
    wheatsum = 0
    ricesum = 0
    combosum = 0
    for i in exp:
        wheatsum+=i.wheat
        ricesum+=i.rice
        combosum+=i.combo
    context = {
        "exps":exp,
        'wheatsum':wheatsum,
        'ricesum':ricesum,
        'combosum':combosum
    }
    
    return render(request,'consumption/stock_exp.html',context)  
 

def search_this_year(request):
    startday = date(date.today().year, 1, 1)
    endday = date(date.today().year, 12, 31)

    
    
    datef = startday
    datet = endday
    exp = Stock.objects.filter(owner=request.user,operation = "consumption",date__range=(datef,datet))
    
    wheatsum = 0
    ricesum = 0
    combosum = 0
    for i in exp:
        wheatsum+=i.wheat
        ricesum+=i.rice
        combosum+=i.combo
    context = {
        "exps":exp,
        'wheatsum':wheatsum,
        'ricesum':ricesum,
        'combosum':combosum
    }
    
    return render(request,'consumption/stock_exp.html',context)  



