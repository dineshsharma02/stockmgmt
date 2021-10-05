from django.shortcuts import render
from .models import Students_Strength5,Students_Strength8

# Create your views here.

def index(request):
    # o = onetofive.objects.all()
    if request.method=="GET":
        context = {
            'c1':Students_Strength5.objects.all()
        }
        return render(request,'students/onetofive.html',context)
    if request.method=="POST":
        c1 = request.POST['student_c1']
        c2 = request.POST['student_c2']
        c3 = request.POST['student_c3']
        c4 = request.POST['student_c4']
        c5 = request.POST['student_c5']
        
        obj, created = Students_Strength5.objects.update_or_create(
            class1=c1,class2=c2,class3=c3,class4=c4,class5=c5
        )
        # Students_Strength5.has_add_permission() 
        obj.save()


        return render(request,'students/onetofive.html') 