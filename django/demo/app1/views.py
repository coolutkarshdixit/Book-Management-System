from django.shortcuts import render, redirect
from django.http import HttpResponse
from app1.models import ContactZ
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from app1.models import BookM
from django.contrib import sessions
# Create your views here.

def home(request):
    return render(request,"index.html")
def about(request):
    return render(request,"about.html")
def contact(request):
    return render(request,"contact.html")
def register(request):
    return render(request,"register.html")

def message(request):
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        contact=request.POST.get("contact")
        message=request.POST.get("message")
        t=name+email+contact+message
        r=ContactZ(name=name, email=email, contact=contact, message=message)
        r.save()
        return render(request,"contact.html",{"msg":"Value Inserted"})

def registeruser(request):
    if request.method=="POST":
        fname=request.POST.get("fname")
        lname=request.POST.get("lname")
        email=request.POST.get("email")
        password=request.POST.get("password")
        #t=fname+lname+email+password
        #return HttpResponse(t)
        try:
            r=User.objects.create_user(first_name=fname, last_name=lname, email=email, username=email, password=password)
            r.save()
            return render(request,"register.html",{'msg':'A/C Created!!'})
        except:
            return render(request,"register.html",{'msg':'Old User !!'})

def userhome(request):
    return render(request,'userhome.html')

def loginuser(request):
    if request.method=="POST":
        email=request.POST.get("email")
        password=request.POST.get("password")
        
        user=authenticate(username=email, password=password)
        if user is not None:
            request.session["uemail"]=email
            #return HttpResponse("Login")
            login(request,user)
            return redirect('/userhome')
        else:
            return HttpResponse("Sorry!! Wrong Email or Password")

def addbook(request):
    return render(request,'add-book.html')

def bookadded(request):
    if request.method=="POST":
        bid=request.POST.get("bid")
        bname=request.POST.get("bname")
        publication=request.POST.get("publication")
        author=request.POST.get("author")
        bcat=request.POST.get("bcat")
        t=bid+bname+publication+author+bcat
        #return HttpResponse(t)
        try:
            r=BookM(bid=bid, bname=bname, publication=publication, author=author, bcat=bcat)
            r.save()
            return render(request,"add-book.html",{"msg":"Book Added !!"})
        except:
            return render(request,"add-book.html",{"msg":"Book Already Added !!"})


def managebook(request):
    r=BookM.objects.all()
    return render(request,'manage-book.html',{'data':r})        


def editbook(request):
    if request.method=="POST":
        eid=request.POST.get("eid")
        r=BookM.objects.get(sn=eid)
        return render(request,'update-book.html',{'data':r})
    

def updatebook(request): 
    if request.method=="POST":
        uid=request.POST.get("uid")
        bid=request.POST.get("bid")
        bname=request.POST.get("bname")
        publication=request.POST.get("publication")
        author=request.POST.get("author")
        bcat=request.POST.get("bcat")  
        r=BookM.objects.filter(sn=uid).update(bid=bid, bname=bname, publication=publication, author=author, bcat=bcat)
        r=BookM.objects.all()
        return render(request,'manage-book.html',{'data':r})
     

def searchbook(request):
    return render(request,"search-book.html") 

def searchrecord(request):
      if request.method=="POST":
        uid=request.POST.get("bid")
        try:
            r=BookM.objects.get(bid=uid)
            r.save()
            return render(request,'search-record.html',{'data':r})
        
        except:
            return render(request,'search-record.html',{"msg":"data not found"})


def userprofile(request):
    name=request.session["uemail"]
    r=User.objects.get(username=name)
    return render(request,"user-profile.html",{'data':r})


def deletebook(request):
    if request.method=="POST":
        uid=request.POST.get("delete")
        BookM.objects.filter(sn=uid).delete()
        r=BookM.objects.all()
        return render(request,'manage-book.html',{'data':r})
     
    
def changepassword(request):
    return render(request,"change-password.html")

def changepass(request):
    if request.method=="POST":
        cpass=request.POST.get("cpass")
        npass=request.POST.get("npass")
        name=request.session["uemail"]

        try:
            r=User.objects.get(username=name)
            r.set_password(npass)
            r.save()
            return render(request,"change-password.html",{'msg':'Password Changed!!!'})
        except:
            return render(request,"change-password.html",{'msg':'Password Changed!!!'})



def logoutuser(request):
    logout(request)
    return render(request,"index.html")
