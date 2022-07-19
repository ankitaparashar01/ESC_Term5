from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse
from typing import List
from .models import *
from django.core.paginator import Paginator
import pymongo
from django.conf import settings
from .checkvalue import *
from .en_decryption import *
import json

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
    msg = reference_number.decode('utf-8')
    return render(request, 'transaction-complete.html',{"msg": msg})
    #return HttpResponse("success")


def check(request):

    return render(request, "checkorder.html")

def display(request):
    #fetch the data
    key = bytes(ref,'utf-8')

    my_client = pymongo.MongoClient("mongodb+srv://test0:test0123456@cluster0.7ypufdn.mongodb.net/?retryWrites=true&w=majority")
    dbname = my_client['ESC']
    collection_name = dbname[ref]
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
    if collection_name.find({}) is None:
        return HttpResponse("success")
    else:
        return HttpResponse("fail")

