from django.shortcuts import render
from app import views
from .models import Empoly
from .models import Client
from .models import Review
from django.http import HttpResponse
# Create your views here.

def landingpage(request):
    adminemail="pragati@gmail.com"
    adminpassword="pragati"
    email=request.POST.get('email')
    password=request.POST.get('password')
    user=Empoly.objects.filter(email=email)
    if (email==adminemail and password==adminpassword):
        #return HttpResponse("Welcome Admin")
        return render(request, 'adminbase.html')
    if user.exists():
        data=Empoly.objects.get(email=email)
        pass1=data.password
        if password==pass1:
            # return HttpResponse("Welcome User")
            return render(request, 'base.html',{'name':data.name,'email':data.email,'password':data.password})
        else:
                return render(request, 'landingpage.html',{'message':'Invalid email and Password'})
    return render(request,'landingpage.html')

def registration(request):
    if request.method == 'POST':
        print(request.POST)
        print(request.FILES)
        name=request.POST.get('username')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        address=request.POST.get('address')
        Specilastion=request.POST.get('specilastion')
        image=request.FILES.get('image')
        password=request.POST.get('password')
        cpassword=request.POST.get('cpassword')
        print(name,email,phone,password,cpassword)
        user = Empoly.objects.filter(email=email)
        if user:
            x = "Email already exist"
            return render(request, 'registration.html', {'msg': x})
        else:
            pass
        if password==cpassword:
            Empoly.objects.create(name=name,email=email,phone=phone,address=address,Specilastion=Specilastion,image=image,password=password,)
            x = "Resgistration succesfully"
            return render(request,'registration.html',{'msg':x})
        else:
            x = "password and cpassword not match"
            return render(request,'registration.html',{'msg':x,'name':name,'email':email,'phone':phone,'address':address,'Specilastion':Specilastion,'image':image})
    else:
        return render(request, 'registration.html')
    return render(request,'registration.html')  


def registration_table(request):
    emp = Empoly.objects.all()
    print(emp)
    return render(request,'registration_table.html',{'data':emp})

def update(request,pk):
    print(pk)
    if request.method=="POST":
         x = Empoly.objects.get(id=pk)
         p = request.POST.get('name')
         q = request.POST.get('email')
         r = request.POST.get('phone')
         s = request.POST.get('address')
         t = request.POST.get('Specilastion')
         u = request.FILES.get('image')
         
         print(u)
         v = request.POST.get('password')
         x.name = p
         x.email = q
         x.phone = r
         x.address = s
         x.Specilastion = t
         x.image = u
         x.password = v
         x.save()
         emp=Empoly.objects.all()
    x=Empoly.objects.get(id=pk)
    print(x)
    
    return render(request,'update.html',{'data4':x})

def delete(request,pk):
    data = Empoly.objects.get(id=pk)
    data.delete()
    emp = Empoly.objects.all()
    return render(request, 'registration_table.html',{'data':emp})


def edit(request,pk):
    print(pk)
    if request.method=="POST":
         x = Empoly.objects.get(id=pk)
         p = request.POST.get('name')
         q = request.POST.get('email')
         r = request.POST.get('phone')
         s = request.POST.get('address')
         t = request.POST.get('Specilastion')
         u = request.POST.get('image')
         
         print(u)
         v = request.POST.get('password')
         x.name = p
         x.email = q
         x.phone = r
         x.address = s
         x.Specilastion = t
         x.image = u
         x.password = v
         x.save()
         emp=Empoly.objects.all()
    x=Empoly.objects.get(id=pk)
    print(x)
    
    return render(request,'update.html',{'data4':x})

def review(request):
     if request.method == "POST":
         print(request.POST)
         print(request.FILES)
         name=request.POST.get('name')
         email=request.POST.get('email')
         rating=request.POST.get('rating')
         review=request.POST.get('review')
         print(name,email,rating,review)
         review1=Review(name=name,email=email,rating=rating,review=review)
         review1.save()
     return render(request, 'review.html')

def review_data(request):
    rve = Review.objects.all()
    print(rve)
    return render(request,'review_data.html',{'review':rve})

    # return render(request,'review_data') 

def appoiment(request):
    cnt = Client.objects.all()
    print(cnt)
    return render(request,'appoiment.html',{'appoiment':cnt})

    # return render(request, 'appoiment.html')

def services(request):
    emp = Empoly.objects.all()
    # print(emp)
    return render(request,'services.html',{'data':emp})

def booking(request):
    if request.method == "POST":
         print(request.POST)
         print(request.FILES)
         name=request.POST.get('name')
         email=request.POST.get('email')
         number=request.POST.get('number')
         text=request.POST.get('text')
         date=request.POST.get('date')
         time=request.POST.get('time')
         print(name,email,number,text,date,time)
         obj=Client(name=name,email=email,number=number,purpose=text,date=date,time=time)
         print(obj)
         obj.save()
         return render(request,'booking.html',{'data2':obj})
    return render(request,'booking.html')
def clientbase(request):
    return render(request,'clientbase.html')
 
def search(request):
    return render(request,'search.html')
 
       