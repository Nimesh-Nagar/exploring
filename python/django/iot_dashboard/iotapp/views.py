from django.shortcuts import render
# from django.http import HttpResponse


# Create your views here.
def index(request):
    # return HttpResponse('<h1>IoT Dashboard Home </h1>')
    return render(request, 'iotapp/index.html')

