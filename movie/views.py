from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    #return httpResponse("<h1>Welcome to the Movie App Home Page!</h1>")
    return render(request,"home.html", {"name":"Camilo"})

def about(request):
    return HttpResponse("<h1>Welcome to the Movie App About Page!</h1>")

