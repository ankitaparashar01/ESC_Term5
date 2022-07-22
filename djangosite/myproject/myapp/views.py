from multiprocessing import context
from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse
from typing import List
from .models import *
from .forms import *
from django.core.paginator import Paginator
import requests
from django.http import HttpResponseRedirect
from .helper import *
import json
from operator import itemgetter


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
    # temporarily hardcoded:
    checkin = "2022-08-20"
    checkout = "2022-08-22"
    guests = "2"

    #generate hotel cards using API 1: 
    # strAPI1 = getAllHotelsPricesWDest(destId, checkin, checkout, guests)
    strAPI1 = str("https://hotelapi.loyalty.dev/api/hotels/prices?destination_id=WD0M&checkin=2022-08-20&checkout=2022-08-22&lang=en_US&currency=SGD&country_code=SG&guests=2&partner_id=1")

    api1Response = requests.get(strAPI1).json()
    # json_data = json.loads(api1Response.text)

    # api1Response = str(api1Response).replace("\'", "\"")

    # Details for each hotel card using API 3:
    # strAPI3 = getSingleHotelRoomTypes(hotelId, destId, checkin, checkout, guests)
    # api3Response = requests.get(strAPI3).json()
    api1Response = json.dumps(api1Response)
    api1Obj = Api1.from_json(api1Response) # create hotel cards from api1Obj.hotels
    

    
     # set up pagination below:
    # p = Paginator(api1Obj, 7) #specify number of cards per page here
    # page = request.GET.get('page',1)
    # listings = p.get_page(page)

    context = {
    # 'listings': listings,
    # 'api1Obj':api1Obj,
    'api1Response':api1Response,
    'api1Obj':api1Obj,
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
    typeOfRoomsJsonStr = str("https://hotelapi.loyalty.dev/api/hotels/diH7/price?destination_id=WD0M&checkin=2022-08-20&checkout=2022-08-22&lang=en_US&currency=SGD&country_code=SG&guests=2&partner_id=1")
    # typeOfRoomsJsonStr = getRoomsHotelInstanceJSON(hotelId, destIdVar, checkin, checkout, guests)
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


# ------------------------------------------- API Classes -------------------------------------------
class Api1:
    def __init__(self, searchCompleted, completed, status, currency, hotels):
        self.searchCompleted = searchCompleted
        self.completed = completed
        self.status = status 
        self.currency = currency 
        self.hotels = hotels #this is a list with dict elements

    @classmethod
    def from_json(cls, json_string):
        json_dict = json.loads(json_string)
        return cls(**json_dict)

    def getTotalHotels(self):
        return len(self.hotels)

    def get_hotel_dict_from_hotels(self, hotelId):
        # e.g. hotelId = "h3z1"
        hotelIdList = list(map(itemgetter('id'), self.hotels)) # generate list of HotelIds
        index = hotelIdList.index(hotelId) # obtain index of a specific HotelId from that list
        hotelJSON = str(self.hotels[index])
        hotelJSON = hotelJSON.replace("\'", "\"") # JSON requires "
        return hotelJSON

class HotelApi1:
    def __init__(self, id, searchRank, price_type, max_cash_payment, coverted_max_cash_payment, points, bonuses, lowest_price, price, converted_price, lowest_converted_price, market_rates):
        self.id = id 
        self.searchRank=searchRank
        self.price_type = price_type
        self.max_cash_payment=max_cash_payment
        self.coverted_max_cash_payment = coverted_max_cash_payment
        self.points=points 
        self.bonuses =bonuses 
        self.lowest_price = lowest_price 
        self.price = price
        self.converted_price=converted_price
        self.lowest_converted_price=lowest_converted_price 
        self.market_rates = market_rates

    @classmethod
    def from_json(cls, json_string):
        json_dict = json.loads(json_string)
        return cls(**json_dict)