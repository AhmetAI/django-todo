from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def user_login(request):
    if request.user.is_authenticated and "next" in request.GET:
        return render(request, "account/login.html")

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
        
            return redirect("index")

        else:
            return render(request, "account/login.html", {"error":"Kullanıcı Adı Veya Parola Yanlış"})

            
    return render(request, "account/login.html")


def user_register(request):
     if request.method=="POST":
         username = request.POST["username"]
         email = request.POST["email"]
         password = request.POST["password"]
         repassword = request.POST["re-password"]

         if password != repassword:
             return render(request, "account/register.html", {"error":"Password is not matched"})
         
         if User.objects.filter(username = username).exists():
             return render(request, "account/register.html", {"error":"This username is used"})
         
         if User.objects.filter(email = email).exists():
             return render(request, "account/register.html", {"error":"This email is used"})
         
         user = User.objects.create_user(username=username, email=email, password=password)
         user.save()
         return redirect("login")
             

     return render(request, "account/register.html")



def user_logout(request):
    logout(request)
    return redirect("index")