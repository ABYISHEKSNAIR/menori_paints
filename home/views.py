from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from  django.http import HttpResponse
# Create your views here.
def index(request):
   return render(request,'index.html')
def about(request):
   return render(request,'about.html')
def products(request):
     return render(request,'products.html')
def interior(request):
         return render(request,'interior.html')
def primer(request):
     return render(request,'primer.html')
def exterior(request):
     return render(request,'exterior.html')       
def dealers(request):
    return render(request,'dealers.html')
def careers(request):
    return render(request,'careers.html')
def contact(request):
   return render(request,'contact.html')