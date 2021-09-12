from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from .forms import LoginForm
from home.models import Contact

# Create your views here.
def loginView(request):
 form = LoginForm()
 if request.method == "POST":
  form = LoginForm(request.POST)
  if form.is_valid():
    username = form.cleaned_data['username']
    password = form.cleaned_data['password']
    user = authenticate(request,username=username,password=password)
    if user is not None:
     login(request,user)
     request.session['username'] = username
     # request.session.set_expiry(15)
     contacts = Contact.objects.all()
     return render(request,'home.html',{'contacts':contacts})

 return render(request,'login.html',{'form':form})


def logoutView(request):
 logout(request)
 contacts = Contact.objects.all()
 return render(request,'home.html',{'contacts':contacts})
