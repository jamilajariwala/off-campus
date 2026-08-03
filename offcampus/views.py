from django.shortcuts import render ,redirect
from django.contrib.auth import login , authenticate, logout
from django.contrib import messages
from django.http import HttpResponse
from django.http import HttpRequest
from .models import *
import random
# Create your views here.
def index(request):
    flat=Flats.objects.all()
    flatran=random.sample(list(flat),3)
    ct=city.objects.all()
    return render(request,"index.html",{'flat':flatran,'ct':ct})
def view_flat(request,id):
    f=Flats.objects.all()
    flatran=random.sample(list(f),3)
    flat=Flats.objects.get(id=id)
    aminitie= flat.aminitie.all()
    return render(request,"view_flat.html",{'flat':flat,'aminitie':aminitie,'f' : flatran})
def viewproperty(request):
    flat=Flats.objects.all()
    flatran=random.sample(list(flat),9)
    return render(request,"view_property.html",{'flat':flatran})
def feedback(request):
    if request.method=="POST":
        nm=request.POST['name']
        mail=request.POST['email']
        no=request.POST['phoneno']
        fd=request.POST['message']
        satisfy=request.POST['satisfy']
        feedback=Feedback.objects.create(username=nm, useremail=mail, userphone=no, satisfy=satisfy, feedback=fd)

        feedback.save()
    return render(request,"fd.html")
def userlogin(request):
    if request.method == "POST":
        nm=request.POST.get('username')
        mail=request.POST.get('email')
        password=request.POST.get('pass')
        user=authenticate(username=nm,email=mail,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            return redirect('/signup')
    
    return render(request,"login.html")
def signup(request):
    if request.method=="POST":
        nm=request.POST['username']
        mail=request.POST['email']
        no=request.POST['phone']
        password=request.POST['pass']
        gen=request.POST['gender']

        user = User.objects.create_user(username=nm,email=mail,password=password)
        signup=userregister.objects.create(user=user,phone=no,gender=gen)

        user.save()
        signup.save()
        return redirect('/login')


    return render(request,'signup.html')
def userlogout(request):
    logout(request)
    return redirect("/")

def Booking(request):
    if request.method=="POST":
        f=request.POST['fnm']
        l=request.POST['lnm']
        sc=request.POST['scno']
        pc=request.POST['pcno']
        se=request.POST['semail']
        pe=request.POST['pemail']
        g=request.POST['gender']
        a=request.POST['address']
        ci=request.POST['checkin']
        co=request.POST['checkout']
        t=request.POST['type']
        p=request.POST['mode']
        booki=My_booking.objects.create(user=request.user,first_name=f,last_name=l,student_cno=sc,parent_cno=pc,student_email=se,parent_email=pe,gender=g,address=a,check_in_date=ci,check_out_date=co,type=t,payment_mode=p)
        booki.save()
        
    return render(request,'booking.html')

def rules(request):
    return render(request,'rules.html')

def view_booking(request):
    b=My_booking.objects.filter(user=request.user)
    return render(request,'view_booking.html',{'b':b})

def cityroom(request,id):
    ct=city.objects.get(id=id)
    flat=Flats.objects.filter(city=ct)
    return render(request,'cityroom.html',{'flat':flat})