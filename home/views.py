import django
from django.shortcuts import render
from .models import Contact
from .forms import AddForm

# Create your views here.
def home(request):
 contacts = Contact.objects.all()
 return render(request,'home.html',{'contacts':contacts})

def add(request):
 form = AddForm()
 if request.method == "POST":
  form = AddForm(request.POST)
  if form.is_valid():
   new_name = form.data.get('name')
   new_relation = form.data.get('relation')
   new_phone = form.data.get('phone')
   new_email = form.data.get('email')
   new_address = form.data.get('address')
   Contact.objects.create(
    name = new_name,
    relation = new_relation,
    phone = new_phone,
    email = new_email,
    address = new_address,
   )
   contacts = Contact.objects.all()
   return render(request,'home.html',{'contacts':contacts})

 return render(request,'add.html',{'form':form})

 