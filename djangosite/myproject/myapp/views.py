from multiprocessing import context
from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse
from typing import List
from .models import *
from .forms import *
from django.core.paginator import Paginator
import requests
from django.http import HttpResponseRedirect


#---------------------FOR LANDING PAGE FORM---------------------
def ascenda(request):
    
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = DestinationCreationForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/hotellistings/')
    
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
    p = Paginator(ListingItem.objects.all(), 7)
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

def confirmation(request, hotelName, hotelId, destId):
    destIdVar = destId # access in HTML using --> <h1>dest uid: {{ destIdVar }}</h1>
    
    #dyanamic JSON Api search for specific Hotel below: 
    jsonHotelStr = str(hotelId)
    jsonHotelRoomBaseStr = str("https://hotelapi.loyalty.dev/api/hotels/")
    jsonReqestInput = jsonHotelRoomBaseStr + jsonHotelStr
    response3HotelInstance = requests.get(jsonReqestInput).json()

    context = {'response3HotelInstance':response3HotelInstance,
    'destIdVar':destIdVar,
    } 

    return render(request, 'confirmation.html', context)


def transactionComplete(request):
    return render(request, 'transaction-complete.html')



#---------------------DATABASE MIGRATIONS---------------------

#hotel search based on chosesn location
def testapi(request, destId):
    destIdVar = destId # access in HTML using --> <h1>dest uid: {{ destIdVar }}</h1>
    
    # accessing destinations.json from mongodb via models.py
    destObj = DestinationCat.objects.get(uid=destIdVar)

    #dyanamic JSON Api search for specific destination: 
    jsonDestStr = str(destId)
    jsonDestBaseStr = str("https://hotelapi.loyalty.dev/api/hotels?destination_id=")
    jsonReqestInput = jsonDestBaseStr + jsonDestStr
    response1 = requests.get(jsonReqestInput).json() 

    # obtaining price for each hotel card
    jsonRequestInputHotelPrices = "https://hotelapi.loyalty.dev/api/hotels/prices?destination_id=WD0M&checkin=2022-08-20&checkout=2022-08-22&lang=en_US&currency=SGD&country_code=SG&guests=2&partner_id=1" 
    response1HotelPrices = requests.get(jsonRequestInputHotelPrices).json()

    # find specific hotel price
    
     # set up pagination below:
    p = Paginator(response1, 7) #specify number of cards per page here
    page = request.GET.get('page',1)
    listings = p.get_page(page)

    context = {'response1':response1,
    'listings': listings,
    # 'dest_list': dest_list,
    'destIdVar':destIdVar,
    'destObj':destObj,
    'response1HotelPrices':response1HotelPrices,
    }

    return render(request,'NEWhotellistings.html', context)

def testapiRoomList(request, hotelName, hotelId, destId):
    destIdVar = destId # access in HTML using --> <h1>dest uid: {{ destIdVar }}</h1>
    
    #dyanamic JSON Api search for specific Hotel below: 
    jsonHotelStr = str(hotelId)
    jsonHotelRoomBaseStr = str("https://hotelapi.loyalty.dev/api/hotels/")
    jsonReqestInput = jsonHotelRoomBaseStr + jsonHotelStr
    response2 = requests.get(jsonReqestInput).json() 

    # available room types generation:
    checkin = "2022-08-20"
    checkout = "2022-08-22"
    guests = "2"
    # typeOfRoomsJsonStr = str("https://hotelapi.loyalty.dev/api/hotels/diH7/price?destination_id=WD0M&checkin=2022-08-20&checkout=2022-08-22&lang=en_US&currency=SGD&country_code=SG&guests=2&partner_id=1")
    typeOfRoomsJsonStr = getRoomsHotelInstanceJSON (hotelId, destIdVar, checkin, checkout, guests)
    response2TypeOfRooms = requests.get(typeOfRoomsJsonStr).json() 


    context = {'response2':response2,
    # 'hotelnamevar' : hotelnamevar,
    'destIdVar':destIdVar,
    'response2TypeOfRooms':response2TypeOfRooms,
    'typeOfRoomsJsonStr':typeOfRoomsJsonStr,
    'jsonHotelStr':jsonHotelStr,
    'destIdVar':destIdVar,
    }

    return render(request,'roomlisttestapi.html', context)

# ---------------------Helper functions---------------------
def getRoomsHotelInstanceJSON (hotelId, destId, checkin, checkout, guests):
    # deafault values
    langStr = "en_US"
    currencyStr = "SGD"
    country_code= "SG"
 
    jsonHotelInstanceRoomAvailBaseStr = str("https://hotelapi.loyalty.dev/api/hotels/")
    # jsonReqestInputHotelPrice = str("https://hotelapi.loyalty.dev/api/hotels/diH7/prices?destination_id={}&checkin={}&checkout={}&lang={}&currency={}&country_code={}&guests={}&partner_id={}").format(destId, checkin, checkout,langStr, currencyStr, country_code, guests, partner_id)
    jsonReqestInputHotelPrice = str(jsonHotelInstanceRoomAvailBaseStr + hotelId + "/price?destination_id=" + destId + "&checkin=" + checkin + "&checkout=" + checkout + "&lang=" + langStr + "&currency=" + currencyStr + "&country_code=" + country_code + "&guests=" + guests + "&partner_id=1")

    return jsonReqestInputHotelPrice


def getHotelPriceJSON(destId, checkin, checkout, guests):
    # example of url for reference, we will be using the format of the FIRST one:
    # JSONStr = "https://hotelapi.loyalty.dev/api/hotels/prices?destination_id=WD0M&checkin=2022-08-20&checkout=2022-08-22&lang=en_US&currency=SGD&country_code=SG&guests=2&partner_id=1" 
    # JSONStr = "https://hotelapi.loyalty.dev/api/hotels/prices?destination_id=WD0M&checkin=2022-08-20&checkout=2022-08-22&lang=en_US&currency=SGD&landing_page=&partner_id=16&country_code=SG&guests=2"
    
    destId = str(destId)
    checkin = str(checkin)
    checkout = str(checkout)
    guests = str(guests)
    
    # deafault values
    langStr = "en_US"
    currencyStr = "SGD"
    country_code= "SG"

    jsonHotelListingsPriceBaseStr = str("https://hotelapi.loyalty.dev/api/hotels/prices?destination_id=")
    jsonRequestHotelListingsPrice = jsonHotelListingsPriceBaseStr + destId + "&checkin=" + checkin + "&checkout=" + checkout + "&lang=" + langStr + "&currency=" + currencyStr + "&country_code=" + country_code + "&guests=" + guests + "&partner_id=1"
    return jsonRequestHotelListingsPrice