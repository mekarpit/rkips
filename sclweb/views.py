from operator import is_not
from django.http import HttpResponse
from django.shortcuts import redirect,  render  , HttpResponse
from sclweb.models import RKIPSLI
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
#from django.contrib import messages
# Create your views here.

def home(request):
    #return HttpResponse("this is homepage")
    return render(request, 'home.html')

def data(request):
    variable = {
        'var1' : 'variable1',
        'var2' : 'variable2'
    }
    return render(request, 'data.html',variable)

def bs(request):
    return render(request, 'bootstrap.html')

def gallery(request):
    return render(request, 'gallery.html')

def coursefee(request):
    return render(request, 'coursefee.html')

def contact(request):
    return render(request, 'contact.html')

def inside(request): 
    print(request.user)
    if request.user.is_anonymous:
        return redirect("/login.html")
    return render(request,'insidepage.html')

def signinuser(request):
    if request.method == 'POST':
        uname=request.POST.get('Lusername')
        pword=request.POST.get('Lpassword')
        print(uname, pword)
        user = authenticate(request,username=uname, password = pword)
        if user is not None:
            print("authenticated")
            login(request, user)
            return redirect("/lin")
        else:
            print('not authenticated')
            return render(request,'login.html')
    return render(request, 'login.html')

def signout(request):
    logout(request)
    return redirect('/')

def signup(request):
    if request.method == 'POST':
        Susername = request.POST.get('SignUpname')
        Spassword = request.POST.get('SignUppassword')
        rkipsli = RKIPSLI(username=Susername, password=Spassword)
        rkipsli.save()
        #messages.success(request, 'SignUp Successfull')
    return render(request, 'signup.html')

