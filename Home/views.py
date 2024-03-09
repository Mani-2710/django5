from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from .models import Admin, Contact


def home(request):
    return render(request,'Home/home.html')

def about(request):
    return render(request,'Home/about.html')

def contactus(request):
    return render(request,'Home/contactus.html')

def login(request):
    return render(request,'Home/login.html')

def Register(request):
    return render(request,'Home/Register.html')
def forgotpassword(request):
    return render(request, 'Home/forgotpassword.html')

def base2(request):
    return render(request,'Home/base2.html')
# def checklogin(request):
#     name = request.POST["username"]
#     password = request.POST["pwd"]
#     flag = Admin.objects.filter(Q(username=name) & Q(password=password))
#     error_message = None
#
#     print(flag)
#
#     if flag:
#         return redirect('Home-home')
#     else:
#         error_message = 'Invaild'
#         return redirect('Home-login')
#     print(username,pwd)
#     return render(request, 'login.html', {'error': error_message})
# def checklogin(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('pwd')
#
#         user = authenticate(request, username=username, password=password)
#
#         if user is not None:
#             # Authentication successful, perform further actions if needed
#             login(request, user)
#         else:
#             # Authentication failed, set an error message
#             error_message = 'Invalid credentials'
#             return render(request, 'Home/login.html', {'error_message': error_message})
def checklogin(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("pwd")
        user_exists = Admin.objects.filter(Q(username=username) & Q(password=password)).exists()

        if user_exists:
            # Authentication successful, redirect to the home page
            return redirect('Home-base')
            #return render(request,"Home/base2.html")
        else:

            # Authentication failed, set an error message
            error_message = 'Invalid credentials'
            return render(request, 'Home/login.html', {'error_message': error_message})



def addregister(request):
    if request.method == 'POST':
        name = request.POST['username']
        password = request.POST['pwd']
        new_id =Admin(username=name, password=password)
        new_id.save()
        return redirect('Home-home')
def contactsave(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message=request.POST['message']
        new_id = Contact(name=name,email=email,message=message)
        new_id.save()
        return redirect('Home-home')
def logout(request):
    request.session.clear()
    return redirect('Home-login')