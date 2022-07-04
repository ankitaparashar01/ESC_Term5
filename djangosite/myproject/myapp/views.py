from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
# def myfunctioncall(request):
#     return HttpResponse("Hello World")

# def myfunctionabout(request):
#     return HttpResponse("About Response")

# def intro(request, name, age):
#     mydictionary = {
#         "name" : name,
#         "age" : age
#     }
#     return JsonResponse(mydictionary)

def ascenda(request):
    return render(request, 'index.html')

def hotellist(request):
    return render(request, 'hotellist.html')

def roomlist(request):
    return render(request, 'roomlist.html')

def confirmation(request):
    return render(request, 'confirmation.html')

