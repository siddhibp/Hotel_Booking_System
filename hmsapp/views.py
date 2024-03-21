from django.shortcuts import render,HttpResponse,redirect
from hmsapp.models import abc
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout



def create(request):
   # print(request.method)
   if request.method == 'GET':
    return render(request,'create.html')
   elif request.method == 'POST':
     #else me post method hai and wo data send krra hai sql me
     name = request.POST['name']
     
     price = request.POST['price']
     
     details = request.POST['detail']
     
     category = request.POST['category']

     image = request.FILES['upload']

     

     M = abc.objects.create(name = name, price = price, details = details, category = category, image = image)  # create method query create krega
     M.save()  #actually save method execute krega

     v = abc.objects.all()
     context = {}
     context['data'] = v
     return render(request,"dashboard.html", context )
 
   
def dashboard(request):
    m= abc.objects.all()
    context = {}
    context['data'] = m
    return render(request,'dashboard.html',context)

def index(request):
       return render(request, 'index.html')


def book(request):
       return render(request, 'book.html')


def delete(request,rid):
    m=abc.objects.filter(id=rid)
    m.delete()
    return redirect('/dashboard')


def edit(request,rid):
    if request.method =='GET':
        m= abc.objects.filter(id= rid)
        context = {}
        context['data'] = m
        return render(request,'edit.html',context)
    else:
        name=request.POST['uname']
        price=request.POST['uprice']
        details=request.POST['udetails']
        category=request.POST['ucategory']
        image =request.FILES['uimage']
        m=abc.objects.filter(id=rid)
        m.update(name = name, price = price,details = details,category=category,image=image)
        return redirect('/dashboard')
    
  

def home(request):
    return render(request,'home.html')

def contact(request):
    return render(request,'contact.html')
def rooms(request):
    return render(request,'rooms.html')



def register(request):
    if request.method == "GET":
        return render(request, 'register.html')
    
    else:
        uname = request.POST['uname']
        uemail = request.POST['uemail']
        upass = request.POST['upass']
        cpass = request.POST['cpass']

        if uname =="" or upass=="" or cpass== "":
            context = {}
            context['msg']= "Field cannot be empty"
            return render(request,'register.html',context)
        
        elif upass != cpass:
            context ={}
            context['msg'] = "Password and confirm password should be same"
            return render(request,'register.html',context)
        else:
            u = User.objects.create(username = uname, email = uemail) 
            u.set_password(upass)
        
            u.save()
           
            
            return redirect("/login")
        

def user_login(request):
   if request.method == "GET":
    return render(request, 'login.html')
   else:
      uname = request.POST['uname']

      upass = request.POST['upass']

      u = authenticate(username = uname, password = upass)
      #u me user ka sara informaation save hai.
      if u is not None:
         login(request, u)
         return redirect('/home')
      else:
         return HttpResponse("user not found")

def user_logout(request):
   logout(request)
   return redirect('/')   

def addproduct(request):
       m = abc.objects.all()
       context = {}
       context['data'] = m
       return render(request,'index.html', context)

 
