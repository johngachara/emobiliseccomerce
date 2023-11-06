from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request,'home.html')
def shoppage(request):
    return render(request,'shop.html')
def aboutuspage(request):
    return render(request,'about.html')