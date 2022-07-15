from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse
from typing import List
from .models import *
from django.core.paginator import Paginator
import requests


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

def confirmation(request):
    return render(request, 'confirmation.html')

def transactionComplete(request):
    return render(request, 'transaction-complete.html')

def testapi(request):
    response1 = requests.get('https://hotelapi.loyalty.dev/api/hotels?destination_id=WD0M').json() # from Mock Static Data endpoints -> Static information of hotels belonging to a destination
    response2 = requests.get('https://hotelapi.loyalty.dev/api/hotels/diH7').json()
    response3 = requests.get('https://hotelapi.loyalty.dev/api/hotels/diH7/price?destination_id=RsBU&checkin=2021-03-31&checkout=2021-04-01&lang=en_US&currency=SGD&partner_id=16&country_code=SG&guests=2').json()
    response4 = requests.get('https://hotelapi.loyalty.dev/api/hotels/prices?destination_id=RsBU&checkin=2021-03-31&checkout=2021-04-01&lang=en_US&currency=SGD&landing_page=&partner_id=16&country_code=SG&guests=2').json()
    context = {'response1':response1,
    'response2':response2,
    'response3':response3,
    'respone4':response4}
    return render(request,'testapi.html',context)

# def testapi(request):
#     response = requests.get('https://hotelapi.loyalty.dev/api/hotels?destination_id=WD0M').json() # from Mock Static Data endpoints -> Static information of hotels belonging to a destination
#     context = {'response':response}
#     return render(request,'testapi.html',context)