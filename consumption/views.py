from django.shortcuts import redirect, render
from .models import Consumption

# Create your views here.
def index(request):
    if request.method=="GET":
        exp = Consumption.objects.filter(owner = request.user)
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
        new_exp = Consumption.objects.create(owner=request.user,date=dor,description=description,wheat = wheat,rice=rice,combo = combo)
        new_exp.save()
        return redirect('stock_exp')


def update_exp(request,id):
    exp = Consumption.objects.get(pk=id)
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
        exp.date=dor
        exp.description=description
        exp.wheat = wheat
        exp.rice=rice
        exp.combo = combo
        exp.save()
    
        return redirect('stock_exp')
        
def delete_exp(request, id):
    exp = Consumption.objects.get(pk=id)
    exp.delete()
    # messages.success(request, "Expense removed")
    return redirect('stock_exp')


# def search_dates(request,startdate,enddate):
#     receipt = Receipt.objects.filter(date=)


