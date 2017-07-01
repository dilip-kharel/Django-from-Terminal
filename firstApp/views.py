from django.shortcuts import render
#from django.http import HttpResponse

def index(request):
   # return HttpResponse("<h2>HEY</h2>")
    return render(request, 'firstApp/home.html')
# Create your views here.
 