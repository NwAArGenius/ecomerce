from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model,login,authenticate,logout

# Create your views here.
User = get_user_model()


def register(request):
  if request.method == "POST":
   username = request.POST.get("username")
   password = request.POST.get("password")
   email = request.POST.get("email")
   user = User.objects.create_user(username=username,password=password,email=email)
   login(request,  user)
   return redirect('home')
  return render(request, 'account/register.html')



def login_user(request):
    if request.method == "POST":
     password = request.POST.get("password")
     email = request.POST.get("email")
     user = authenticate(password=password,emial=email)
     if user:
         login(request, user)
     return redirect('home')
    return render(request , 'account/login.html')



def logout_user(request):
    logout(request)
    return redirect('home')