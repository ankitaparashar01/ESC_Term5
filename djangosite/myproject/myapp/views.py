from multiprocessing import context
from django.forms import NullBooleanField
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
import ast
from django.views.generic.edit import FormView
from django.urls import reverse_lazy



#---------------------FOR LANDING PAGE FORM---------------------
def ascenda(request):
    
    context = {
    }
    return render(request, 'index.html', context)


#---------------------FOR FORM SUBMISSION RESULTS---------------------
def submitmyform(request):
    mydictionary = {
        "var1" : request.POST['destinationorhotel'],
        "var2" : request.POST['calendarCheckin'],
        "var3" : request.POST['calendarCheckout'],
        "var4" : request.POST['roomsnumber'],
        "var5" : request.POST['adultsnumber'],
        "var6" : request.POST['childrennumber'],
        "method" : request.method
    }
    return JsonResponse(mydictionary)
    

#---------------------FOR CONFIRMATION AND PAYMENT---------------------

def confirmation(request, destId, hotelName, hotelId, roomKey, roomType):
    # hardcoded values:
    checkin = "2022-08-20"
    checkout = "2022-08-22"
    guests = "2"

    # Using API 2 to obtain rooms info:
    strAPI2 = getSingleHotelRoomTypes(hotelId, destId, checkin, checkout, guests)
    # strAPI2 = "https://hotelapi.loyalty.dev/api/hotels/diH7/price?destination_id=WD0M&checkin=2022-08-20&checkout=2022-08-22&lang=en_US&currency=SGD&country_code=SG&guests=2&partner_id=1"    
    api2Response = requests.get(strAPI2).json()
    api2Response = json.dumps(api2Response)
    api2Obj = Api2.from_json(api2Response) # create room cards from api1Obj.rooms

    # Using RoomsApi2 to obtain specific room info based on "key":
    chosenRoomJSON = api2Obj.get_room_dict_from_hotels(roomKey, roomType)
    
    chosenRoomObj = RoomsApi2.from_json(chosenRoomJSON)

    context = {'destId':destId,
    'hotelName':hotelName,
    'hotelId':hotelId,
    'roomKey':roomKey,
    'api2Obj':api2Obj,
    'checkin':checkin,
    'checkout':checkout,
    'guests':guests,
    'chosenRoomObj':chosenRoomObj,
    } 
    return render(request, 'confirmation.html', context)


def transactionComplete(request):
    return render(request, 'transaction-complete.html')


#hotel search based on chosesn location
def hotelCards(request, destId):
    destId = str(destId)
    
    # temporarily hardcoded:
    checkin = "2022-08-20"
    checkout = "2022-08-22"
    guests = "2"

    #generate hotel cards using API 1: 
    strAPI1 = getAllHotelsPricesWDest(destId, checkin, checkout, guests)
    # strAPI1 = str("https://hotelapi.loyalty.dev/api/hotels/prices?destination_id=WD0M&checkin=2022-08-20&checkout=2022-08-22&lang=en_US&currency=SGD&country_code=SG&guests=2&partner_id=1")
    api1Response = requests.get(strAPI1).json()
    api1Response = json.dumps(api1Response)
    api1Obj = Api1.from_json(api1Response) # create hotel cards from api1Obj.hotels
    
    
    
    # set up pagination below:
    p = Paginator(api1Obj.hotels, 7) #specify number of cards per page here
    page_number = request.GET.get('page')
    page_obj = p.get_page(page_number)

    if request.htmx:
        template_name = "partials/hotelcardelement.html"
    else:
        template_name = "NEWhotellistings.html"

    context = {
    'page_obj': page_obj,
    'api1Response': api1Response,
    'api1Obj': api1Obj,
    'destId': destId,
    }

    return render(request, template_name, context)

def RoomList(request, destId, hotelName, hotelId):
    # hardcoded values:
    checkin = "2022-08-20"
    checkout = "2022-08-22"
    guests = "2"
    
    # Using API 2 to generate room cards:
    strAPI2 = getSingleHotelRoomTypes(hotelId, destId, checkin, checkout, guests)
    # strAPI2 = "https://hotelapi.loyalty.dev/api/hotels/diH7/price?destination_id=WD0M&checkin=2022-08-20&checkout=2022-08-22&lang=en_US&currency=SGD&country_code=SG&guests=2&partner_id=1"    
    api2Response = requests.get(strAPI2).json()
    api2Response = json.dumps(api2Response)
    api2Obj = Api2.from_json(api2Response) # create room cards from api1Obj.rooms
    roomNamesList = api2Obj.get_present_room_names_list()

    # Using API 3 to generate info about the hotel:
    strAPI3 = getHotelCardWHotelID(hotelId)
    # strAPI3 = "https://hotelapi.loyalty.dev/api/hotels/diH7"
    api3Response = requests.get(strAPI3).json()
    api3Response.pop('hires_image_index', None) # 'hires_image_index' is removed should it exist. else, do nothing

    api3Response = json.dumps(api3Response)
    api3Obj = Api3.from_json(api3Response) # create room cards from api1Obj.rooms

    context = {'destId':destId,
    'hotelId':hotelId,
    'api2Obj':api2Obj,
    'api3Obj': api3Obj,
    'roomNamesList':roomNamesList,
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
    
    def get_hotel_index(self, hotelId):
        hotelIdList = list(map(itemgetter('id'), self.hotels)) # generate list of HotelIds
        index = hotelIdList.index(hotelId)
        return index

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

"""how to get the indiv card details? we are currently using 2 different apis.
api 1 retrieves the respective hotel price.
then on that card there will be the hotel id from api 1
i want to use that hotel id to access the card details from api 3.
{{hotelCard.id}}"""

class Api2:
    def __init__(self, searchCompleted, completed, status, currency, rooms):
        self.searchCompleted = searchCompleted
        self.completed = completed
        self.status = status 
        self.currency = currency 
        self.rooms = rooms #this is a list with dict elements

    @classmethod
    def from_json(cls, json_string):
        json_dict = json.loads(json_string)
        return cls(**json_dict)
    
    def getTotalRooms(self):
        return len(self.rooms)

    def get_diff_room_types_list(self):
        typeList = list(map(itemgetter('type'), self.rooms))
        typeList = list(set(typeList))
        return typeList

    def get_present_room_names_list(self):
        roomNameList = list(map(itemgetter('roomNormalizedDescription'), self.rooms))
        roomNameList = list(set(roomNameList))
        return roomNameList

    def get_list_of_room_keys(self):
        keyList = list(map(itemgetter('key'), self.rooms))
        keyList = list(set(keyList))
        return keyList

    def get_room_dict_from_hotels(self, roomKey, roomType):
        # This method returns a specific room dict from api 3
        # e.g. key = "51BFDA0AAABACE7C11B393FCE438BBA3"
        RoomIdList = list(map(itemgetter('type'), self.rooms)) # generate list of room "key"s
        index = RoomIdList.index(roomType) # obtain index of a specific "key" from that list
        roomJSON = str(self.rooms[index])
        roomJSON = ast.literal_eval(roomJSON)
        roomJSON.pop('long_description', None) # remove 'long_description' key since some hotels may not have it and cause the code to break

        # --- clean JSON ---
        # change True to "True" 
        if roomJSON["free_cancellation"] == "true":
            roomJSON["free_cancellation"] = "True"
        elif roomJSON["free_cancellation"] == "false":
            roomJSON["free_cancellation"] = "False"

        # change null to "NULL"
        if roomJSON["roomDescription"] == "null":
            roomJSON["roomDescription"] = "NULL"
        for key in roomJSON["roomAdditionalInfo"]["displayFields"]:
            if roomJSON["roomAdditionalInfo"]["displayFields"][key] == "null":
                roomJSON["roomAdditionalInfo"]["displayFields"][key] = "NULL"

        # roomJSON = roomJSON.replace("\'", "\"") # JSON requires "
        roomJSON = json.dumps(roomJSON)
        
        return roomJSON

class RoomsApi2:
    def __init__(self, key,roomNormalizedDescription,roomDescription, type, free_cancellation,
    roomAdditionalInfo, description, images, amenities, price_type, max_cash_payment, coverted_max_cash_payment,
     points,bonuses, lowest_price, price, converted_price, lowest_converted_price, chargeableRate,
     market_rates):
     self.key = key
     self.roomDescription = roomDescription #could be null
     self.roomNormalizedDescription=roomNormalizedDescription
     self.type =type
     self.free_cancellation=free_cancellation
     self.roomAdditionalInfo=roomAdditionalInfo #dict
     self.description=description
     self.images =images #list of dictionaries
     self.amenities=amenities # list of string
     self.price_type=price_type
     self.max_cash_payment=max_cash_payment
     self.coverted_max_cash_payment=coverted_max_cash_payment
     self.points = points
     self.bonuses =bonuses
     self.lowest_price=lowest_price
     self.price=price
     self.converted_price=converted_price
     self.lowest_converted_price=lowest_converted_price
     self.chargeableRate=chargeableRate
     self.market_rates=market_rates # list of dictionaries
    #  self.long_description = long_description

    @classmethod
    def from_json(cls, json_string):
        json_dict = json.loads(json_string)
        return cls(**json_dict)

class Api3:
    def __init__(self, id, imageCount, latitude,longitude, name, address,address1,rating, trustyou,
     categories, amenities_ratings, description, amenities, original_metadata, image_details
     ,number_of_images, default_image_index, imgix_url, cloudflare_image_url):

        self.id = id
        self.imageCount = imageCount
        self.latitude = latitude
        self.longitude = longitude
        self.name = name
        self.address = address
        self.address1 = address1
        self.rating = rating
        self.trustyou = trustyou
        self.categories = categories
        self.amenities_ratings = amenities_ratings
        self.description = description
        self.amenities = amenities
        self.original_metadata = original_metadata
        self.image_details = image_details
        # self.hires_image_index = hires_image_index
        self.number_of_images = number_of_images
        self.default_image_index = default_image_index
        self.imgix_url = imgix_url # String
        self.cloudflare_image_url = cloudflare_image_url # String

    @classmethod
    def from_json(cls, json_string):
        json_dict = json.loads(json_string)
        return cls(**json_dict)

class HotelCard:
    def __init__(self, hotelId, lowest_price, hotelName):
        self.hotelId = hotelId
        self.lowest_price = lowest_price
        self.hotelName = hotelName
