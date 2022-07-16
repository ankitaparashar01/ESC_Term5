from multiprocessing import context
from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse
from typing import List
from .models import *
from .forms import *
from django.core.paginator import Paginator
import requests

#---------------------FOR LANDING PAGE FORM---------------------
def ascenda(request):
    dest = DestinationCat.objects.all()
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = DestinationCreationForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            # return HttpResponseRedirect('/thanks/')
            return None

    # if a GET (or any other method) we'll create a blank form
    else:
        form = DestinationCreationForm()

    context = {'form': form,
    }
    return render(request, 'index.html', context)


#---------------------FOR HOTEL LISTING SEARCH RESULTS---------------------
def all_listings(request):
    hotels_list = ListingItem.objects.all()
    
    # set up pagination below:
    p = Paginator(ListingItem.objects.all(), 3)
    page = request.GET.get('page')
    listings = p.get_page(page)

    context = {'hotels_list': hotels_list,
    'listings': listings}

    return render(request, 'hotellist.html', context)


#---------------------FOR ROOM TYPE PAGE---------------------
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



#---------------------FOR CONFIRMATION AND PAYMENT---------------------

def confirmation(request):
    return render(request, 'confirmation.html')

def transactionComplete(request):
    return render(request, 'transaction-complete.html')



#---------------------DATABASE MIGRATIONS---------------------

#hotel search based on chosesn location
def testapi(request):
    # jsonDestStr = "destination_id=id=WD0M" #THIS IS HARDCODED FOR NOW --> set to Singapore
    # jsonDestBaseStr = "https://hotelapi.loyalty.dev/api/hotels?"
    # jsonReqestInput = jsonDestBaseStr + jsonDestStr
    # response1 = requests.get(str(jsonReqestInput)).json() 
    
    # DESTINATION HERE IS HARDCODED!!
    response1 = requests.get("https://hotelapi.loyalty.dev/api/hotels?destination_id=WD0M").json() # from Mock Static Data endpoints -> Static information of hotels belonging to a destination


     # set up pagination below:
    p = Paginator(response1, 3)
    page = request.GET.get('page',1)
    listings = p.get_page(page)


    # response1 = requests.get('https://hotelapi.loyalty.dev/api/hotels?destination_id=WD0M').json() # from Mock Static Data endpoints -> Static information of hotels belonging to a destination
    # response2 = requests.get('https://hotelapi.loyalty.dev/api/hotels/diH7').json() # chosen hotel is fullerton
    # response3 = requests.get('https://hotelapi.loyalty.dev/api/hotels/diH7/price?destination_id=RsBU&checkin=2021-03-31&checkout=2021-04-01&lang=en_US&currency=SGD&partner_id=16&country_code=SG&guests=2').json()
    # response4 = requests.get('https://hotelapi.loyalty.dev/api/hotels/prices?destination_id=RsBU&checkin=2021-03-31&checkout=2021-04-01&lang=en_US&currency=SGD&landing_page=&partner_id=16&country_code=SG&guests=2').json()
    context = {'response1':response1,
    # 'response2':response2,
    # 'response3':response3,
    # 'respone4':response4
    'listings': listings,
    }
    return render(request,'testapi.html', context)

def testapiRoomList(request, hotelName, hotelId):
    #dyanamic JSON Api search for specific Hotel below: 
    jsonHotelStr = str(hotelId)
    jsonHotelRoomBaseStr = str("https://hotelapi.loyalty.dev/api/hotels/")
    jsonReqestInput = jsonHotelRoomBaseStr + jsonHotelStr
    response2 = requests.get(jsonReqestInput).json() 
    

    context = {'response2':response2,
    # 'hotelnamevar' : hotelnamevar,
    }
    return render(request,'roomlisttestapi.html', context)


