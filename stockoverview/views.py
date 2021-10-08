from django.shortcuts import render,redirect
import json
import receipt
from .models import Stock
from operator import attrgetter
from itertools import chain
from datetime import date,timedelta
import datetime
import calendar
from django.http import JsonResponse

# Create your views here.
def index(request):
    receipts = Stock.objects.filter(owner=request.user,operation='receipt')
    exps = Stock.objects.filter(owner=request.user,operation='consumption')
    result_list = sorted(chain(receipts, exps),key=attrgetter('date'))
    receipt = 'receipt'
    consumption = 'consumption'
    today = date.today
    receiptwheatsum=0
    receiptricesum=0
    receiptcombosum=0
    expwheatsum=0
    exptricesum=0
    expcombosum=0
    for r in receipts:
        receiptwheatsum+=r.wheat
        receiptricesum+=r.rice
        receiptcombosum+=r.combo

    for e in exps:
        expwheatsum+=e.wheat
        exptricesum+=e.rice
        expcombosum+=e.combo    
    
    netwheat = receiptwheatsum-expwheatsum
    netrice = receiptricesum-exptricesum
    netcombo = receiptcombosum-expcombosum
    context = {
        'stocks':result_list,
        'receipt' : receipt,
        'consumption' : consumption,
        'today': today,
        'netwheat':netwheat,
        'netrice':netrice,
        'netcombo':netcombo,

    }

    return render(request,'stockow/index.html',context)

def get_sum_values(receipt,exp):
    wheatsum = 0
    ricesum = 0
    combosum = 0
    for i in receipt:
        wheatsum+=i.wheat
        ricesum+=i.rice
        combosum+=i.combo

    for i in exp:
        wheatsum-=i.wheat
        ricesum-=i.rice
        combosum-=i.combo

   
    return [wheatsum,ricesum,combosum]


def search_dates(request):
    if request.method=="POST":
        datef = request.POST['datef']
        datet = request.POST['datet']
        receipt = Stock.objects.filter(owner=request.user,operation = "receipt",date__range=(datef,datet))
        exp = Stock.objects.filter(owner=request.user,operation = "consumption",date__range=(datef,datet))
        result_list = sorted(chain(receipt, exp),key=attrgetter('date'))
        
        wheatsum = get_sum_values(receipt,exp)[0]
        ricesum = get_sum_values(receipt,exp)[1]
        combosum = get_sum_values(receipt,exp)[2]
        

        context = {
            "stocks":result_list,
            'netwheat':wheatsum,
            'netrice':ricesum,
            'netcombo':combosum,
            
        }
        
        return render(request,'stockow/index.html',context)

    if request.method=="GET":
        return redirect('stock_overview')    

def search_last_seven_days(request):
    datef = date.today()- timedelta(7)
    datet = date.today()
    
    receipt = Stock.objects.filter(owner=request.user,operation = "receipt",date__range=(datef,datet))
    exp = Stock.objects.filter(owner=request.user,operation = "consumption",date__range=(datef,datet))
    result_list = sorted(chain(receipt, exp),key=attrgetter('date'))
    wheatsum = get_sum_values(receipt,exp)[0]
    ricesum = get_sum_values(receipt,exp)[1]
    combosum = get_sum_values(receipt,exp)[2]
    context = {
        "stocks":result_list,
        'netwheat':wheatsum,
        'netrice':ricesum,
        'netcombo':combosum
    }
    return render(request,'stockow/index.html',context)


def search_last_month(request):

    last_day_of_prev_month = date.today().replace(day=1) - timedelta(days=1)
    start_day_of_prev_month = date.today().replace(day=1) - timedelta(days=last_day_of_prev_month.day)
    datef = start_day_of_prev_month
    datet = last_day_of_prev_month
    receipt = Stock.objects.filter(owner=request.user,operation = "receipt",date__range=(datef,datet))
    exp = Stock.objects.filter(owner=request.user,operation = "consumption",date__range=(datef,datet))
    result_list = sorted(chain(receipt, exp),key=attrgetter('date'))
    wheatsum = get_sum_values(receipt,exp)[0]
    ricesum = get_sum_values(receipt,exp)[1]
    combosum = get_sum_values(receipt,exp)[2]
    context = {
        "stocks":result_list,
        'netwheat':wheatsum,
        'netrice':ricesum,
        'netcombo':combosum
    }
    return render(request,'stockow/index.html',context)    




def search_this_month(request):
    today = date.today()
    start_day_of_this_month = date.today().replace(day=1)
    last_day_num = calendar.monthrange(today.year,today.month)[1]
    last_day_of_this_month = today.replace(day=last_day_num)

    datef = start_day_of_this_month
    datet = last_day_of_this_month
    receipt = Stock.objects.filter(owner=request.user,operation = "receipt",date__range=(datef,datet))
    exp = Stock.objects.filter(owner=request.user,operation = "consumption",date__range=(datef,datet))
    result_list = sorted(chain(receipt, exp),key=attrgetter('date'))
    wheatsum = get_sum_values(receipt,exp)[0]
    ricesum = get_sum_values(receipt,exp)[1]
    combosum = get_sum_values(receipt,exp)[2]
    context = {
        "stocks":result_list,
        'netwheat':wheatsum,
        'netrice':ricesum,
        'netcombo':combosum
    }
    return render(request,'stockow/index.html',context)  
 

def search_this_year(request):
    startday = date(date.today().year, 1, 1)
    endday = date(date.today().year, 12, 31)
    datef = startday
    datet = endday
    receipt = Stock.objects.filter(owner=request.user,operation = "receipt",date__range=(datef,datet))
    exp = Stock.objects.filter(owner=request.user,operation = "consumption",date__range=(datef,datet))
    result_list = sorted(chain(receipt, exp),key=attrgetter('date'))
    wheatsum = get_sum_values(receipt,exp)[0]
    ricesum = get_sum_values(receipt,exp)[1]
    combosum = get_sum_values(receipt,exp)[2]
    context = {
        "stocks":result_list,
        'netwheat':wheatsum,
        'netrice':ricesum,
        'netcombo':combosum
    }
    return render(request,'stockow/index.html',context)

def search_in_overview(request):
    if request.method == 'POST':
        search_str = json.loads(request.body).get('searchText')
        stock = Stock.objects.filter(wheat__istartswith=search_str, owner=request.user) |   Stock.objects.filter(
                                    rice__istartswith=search_str, owner=request.user) | Stock.objects.filter(
                                    combo__istartswith=search_str, owner=request.user) | Stock.objects.filter(
                                    date__istartswith=search_str, owner=request.user) | Stock.objects.filter(
                                    description__icontains=search_str, owner=request.user) | Stock.objects.filter(
                                    operation__icontains=search_str, owner=request.user)

        data = stock.values()
        return JsonResponse(list(data),safe=False)
