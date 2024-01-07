from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def home_view(request):
    title  = "home"
    employees = Employees.objects.all()
    count = Employees.objects.count()
    
    return render(request, "home.html", {"title": title, "employees": employees, "count": count})

def add_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        address = request.POST.get("address")
        phone = request.POST.get("phone")
        
        emp = Employees(name=name, email=email, address=address, phone=phone)
        emp.save()
        return redirect("home")
        
    return render(request, "home.html")

def update_view(request, id):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        address = request.POST.get("address")
        phone = request.POST.get("phone")

        emp = Employees(id=id, name=name, email=email, address=address, phone=phone)
        emp.save()
        return redirect("home")
        
    return render(request, "home.html")

def delete_view(request, id):
    emp = Employees.objects.filter(id=id)
    
    emp.delete()
    return redirect("home")
    print("employee deleted successfully")
    
    return render(request, "home.html")