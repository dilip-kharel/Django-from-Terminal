from django.shortcuts import render

def jam(request):
    return render(request, 'secApp/songShare.html')