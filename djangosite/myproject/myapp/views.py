from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse
from typing import List
from .models import *
from django.core.paginator import Paginator

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

# def hotellist(request):
#     return render(request, 'hotellist.html')

# def roomlist(request):
#     return render(request, 'roomlist.html')

def confirmation(request):
    return render(request, 'confirmation.html')



def all_listings(request):
    hotels_list = ListingItem.objects.all()
    
    # set up pagination below:
    p = Paginator(ListingItem.objects.all(), 3)
    page = request.GET.get('page')
    listings = p.get_page(page)

    context = {'hotels_list': hotels_list,
    'listings': listings}

    return render(request, 'hotellist.html', context)

def roomListPage(request, hotelname):
    # if(ListingItem.objects.filter(name=hotelname)): #url matches the hotelname
    #     hotelname = ListingItem.objects.all()
    #     context = {'hotelname' : hotelname}
    # else:
    #     # messages.error(request, "No such product found")
    #     return redirect('listings')
    hotelnamevar = ListingItem.objects.get(name=hotelname)
    context = {'hotelnamevar' : hotelnamevar}

    return render(request, 'roomlist.html', context)

