from multiprocessing import context
from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse, response
from typing import List
from .models import *
from .forms import *
from django.core.paginator import Paginator
import requests
from django.http import HttpResponseRedirect
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from .helper import *
import json
from operator import itemgetter
import ast
import pymongo
from django.conf import settings
from .checkvalue import *
from .en_decryption import *



#---------------------FOR LANDING PAGE FORM---------------------
def ascenda(request):

    # template_name = "index.html"
    # form_class = SearchHotelForm

    # def form_valid(self,form):
    #     destination = form.cleaned_data.get("destination")
    #     checkin_date = form.cleaned_date.get("checkin_date")
    #     checkout_date = form.cleaned_date.get("checkout_date")
    #     rooms = form.cleaned_data.get("rooms")
    #     adults = form.cleaned_data.get("adults")
    #     children = form.cleaned_data.get("children")

    #     user = User.objects.create_user(destination,checkin_date,checkout_date,rooms,adults,children)
    #     form.instance.user = user

    #     return super().form_valid(form)

    if 'term' in request.GET:
        qs = DestinationCat.objects.filter(term__istartswith=request.GET.get('term'))
        destinationOrHotel = list()
        for product in qs:
            destinationOrHotel.append(product.term)
        # titles = [product.title for product in qs]
        return JsonResponse(destinationOrHotel, safe=False)

    context = {
    }

    return render(request, 'index.html', context)

#---------------------FOR FORM SUBMISSION RESULTS---------------------
def submitmyform(request):
    
    formSearchInputsDict = {
        "destinationorhotel" : request.GET['destId'],
        "checkin" : request.GET['checkin'],
        "checkout" : request.GET['checkout'],
        "roomsnumber" : request.GET['roomsnumber'],
        "adultsnumber" : request.GET['adultsnumber'],
        "childrennumber" : request.GET['childrennumber'],
        # "method" : request.method
    }

    context = {
        'formSearchInputsDict':formSearchInputsDict,
    }

    return render(request, 'submitmyformtest.html', context)
    


# def myform2(request):
#     if request.method == "POST":
#         pass
#     elif request.method == "GET":
#         form = SearchHotelForm()
#         mydictionary = {
#             "form" :form 
#         }
#         return render(request, 'myform2.html', context=mydictionary)
        

#-------------------------------------FOR CONFIRMATION AND PAYMENT-------------------------------------
def confirmation(request, destId, hotelName, hotelId, roomKey, roomType, checkin, checkout, guests):
    # # hardcoded values:
    # checkin = "2022-08-20"
    # checkout = "2022-08-22"
    # guests = "2"

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

#-------------------------------------FOR TRANSACTION COMPLETE-------------------------------------
def transactionComplete(request):
    msg = reference_number.decode('utf-8')
    return render(request, 'transaction-complete.html',{"msg": msg})

def ajax(request):
    global reference_number
    to_check = {}
    empty_check = True
    for i in request.GET.items():
        to_check[i[0]] = i[1]
        if check_not_empty(i[1]) == False:
            empty_check = False
    phonenumber = to_check['CountryCode'] + to_check['PhoneNumber']

    #check validity
    if (check_title(to_check['Title']) 
        and check_cvv(to_check["CVV"]) 
        and check_expire(to_check['ExpireYear'], to_check['ExpireMonth']) 
        and check_phonenumber(phonenumber)
        and check_cardnumber(to_check['CardNumber'])
        and empty_check):
        #generating key
        
        reference_number = generating_key()
        #encrypt data
        for k, v in to_check.items():
            if k != 'CardNumber':
                to_check[k] = encryption(v, reference_number)
            else:
                to_check['CardNumber'] = mask(v)
        #push to database
        my_client = pymongo.MongoClient("mongodb+srv://test0:test0123456@cluster0.7ypufdn.mongodb.net/?retryWrites=true&w=majority")
        dbname = my_client['ESC']
        collection_name = dbname[reference_number.decode('utf-8')]
        collection_name.insert_one(to_check)
        
        return HttpResponse("success")

    else:
        return HttpResponse("failure")

    #每个人都是一个collection，对应的reference number，需要的时候直接去取对应的collection'

def ajax2(request):
    global ref
    ref = request.GET['ID']
    my_client = pymongo.MongoClient("mongodb+srv://test0:test0123456@cluster0.7ypufdn.mongodb.net/?retryWrites=true&w=majority")
    dbname = my_client['ESC']
    collection_name = dbname[ref]
    if len(list(collection_name.find({}))) == 0:
        return HttpResponse("fail")
    else:
        return HttpResponse("success")

#---------------------CHECK ORDER-----------------------      
def check(request):
    return render(request, "checkorder.html")


def display(request):
    #fetch the data
    global ref
    key = bytes(ref,'utf-8')

    my_client = pymongo.MongoClient("mongodb+srv://test0:test0123456@cluster0.7ypufdn.mongodb.net/?retryWrites=true&w=majority")
    dbname = my_client['ESC']
    collection_name = dbname[ref]
    ref = None
    order_details = list(collection_name.find({}))
    doc = order_details[0]
    doc.pop("_id")
    for k,v in doc.items():
        if k != 'CardNumber':
            doc[k] = decryption(v,key)

    #decrypt
    #for k, v in doc.items():
     #   if k != 'CardNumber':
      #      doc[k] = decryption(v, key)
    #
    #render in the html file 
    return render(request, 'display.html',doc)
    #取回数据 generate form



#---------------------HOTEL SEARCH FILTERING-----------------------
def featureOne(request):
    if request.method=="POST":
        destinationorhotel = request.POST['destinationorhotel'],
        calendarCheckin = request.POST['calendarCheckin'],
        calendarCheckout = request.POST['calendarCheckout'],
        roomsnumber = request.POST['roomsnumber'],
        adultsnumber = request.POST['adultsnumber'],
        childrennumber = request.POST['childrennumber'],

    HotelSearch.objects.filter(destinationorhotel=destinationorhotel).update(calendarCheckin=calendarCheckin,calendarCheckout=calendarCheckout,roomsnumber=roomsnumber,adultsnumber=adultsnumber,childrennumber=childrennumber)
    global Qdestinationorhotel, QcalendarCheckin, QcalendarCheckout, Qroomsnumber, Qadultsnumber, Qchildrennumber
    def Qdestinationorhotel():
        return destinationorhotel
    def QcalendarCheckin():
        return calendarCheckin
    def QcalendarCheckout():
        return calendarCheckout
    def Qroomsnumber():
        return roomsnumber
    def Qadultsnumber():
        return adultsnumber
    def Qchildrennumber():
        return childrennumber

    destinationorhotel_entry = HotelSearch.objects.filter(destinationorhotel=destinationorhotel).first()
    dest_id = destinationorhotel_entry.uid
    def Qdest_id():
        return dest_id

    return render(request, 'index.html')

#-------------------------------------FOR HOTEL CARDS-------------------------------------
#hotel search based on chosesn location
def hotelCards(request, destId=None):
    
    formSearchInputsDict = {
        "destinationorhotel" : request.GET['destinationorhotel'],
        "checkin" : request.GET['checkin'],
        "checkout" : request.GET['checkout'],
        "roomsnumber" : request.GET['roomsnumber'],
        "adultsnumber" : request.GET['adultsnumber'],
        "childrennumber" : request.GET['childrennumber'],
    }
    
    
    destinationOrHotel = formSearchInputsDict["destinationorhotel"]
    # print(destinationOrHotel)
    destId = str(convertTermToDestId(destinationOrHotel))
    guests = str(int(formSearchInputsDict["adultsnumber"]) + int(formSearchInputsDict["childrennumber"]))
    checkin = formSearchInputsDict["checkin"]
    checkout = formSearchInputsDict["checkout"]
    rooms = formSearchInputsDict["roomsnumber"]

    

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
    'guests':guests,
    'checkin':checkin,
    'checkout':checkout,
    'rooms':rooms,
    'formSearchInputsDict':formSearchInputsDict,
    }

    return render(request, template_name, context)



#-------------------------------------FOR ROOM CARDS -------------------------------------
def RoomList(request, destId, hotelName, hotelId, checkin, checkout, guests):
    # # hardcoded values:
    # checkin = "2022-08-20"
    # checkout = "2022-08-22"
    # guests = "2"
    
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

    # totalRooms = api2Obj.getTotalRooms()

    context = {'destId':destId,
    'hotelId':hotelId,
    'api2Obj':api2Obj,
    'api3Obj': api3Obj,
    'roomNamesList':roomNamesList,
    'checkin':checkin,
    'checkout':checkout,
    'guests':guests,

    # 'totalRooms':totalRooms,
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


