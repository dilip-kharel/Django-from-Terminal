from django.shortcuts import render
#from django.http import HttpResponse

def index(request):
   # return HttpResponse("<h2>HEY</h2>")
    return render(request, 'firstApp/home.html')

def contact(request):
    return render(request, 'firstApp/basic.html', {'Items':['If you would like to contact me, please email me', 'blabla@bla.com']})