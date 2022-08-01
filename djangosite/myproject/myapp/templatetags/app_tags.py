from django import template
from myapp.helper import *
import requests

register  = template.Library()


# --------------------------- Render hotel card details form Api 3 ---------------------------
def render_name_api3(hotelId):
    # input will be from {{ hotelCard.id }}

    strAPI3 = getHotelCardWHotelID(hotelId)
    # reference = "https://hotelapi.loyalty.dev/api/hotels/diH7
    api3Response = requests.get(strAPI3).json()
    hotelName = api3Response["name"]


    # need to obtain: name, address, address1, rating, 
    return "{}".format(hotelName)
register.filter('render_name_api3', render_name_api3)

def breakfast_avail_bool(breakfastStr):
    setBreakfastStr =""
    if breakfastStr == "hotel_detail_breakfast_included":
        setBreakfastStr = "Breakfast Included"
    elif breakfastStr == "hotel_detail_room_only":
        setBreakfastStr = "Room Only"

    return setBreakfastStr
register.filter('breakfast_avail_bool', breakfast_avail_bool)

# --------------------------- Create image urls list form Api 3 ---------------------------
def list_image_details_api3(hotelId):
    # Return image List

    strAPI3 = getHotelCardWHotelID(hotelId)
    # reference = "https://hotelapi.loyalty.dev/api/hotels/diH7

#     "image_details": {
#     "suffix": ".jpg",
#     "count": 56,
#     "prefix": "https://d2ey9sqrvkqdfs.cloudfront.net/diH7/"
#   },
    api3Response = requests.get(strAPI3).json()
    image_detailsJSON = api3Response["image_details"]
    imageListStr = []
    count = int(image_detailsJSON["count"])
    for i in range(count):
        formImageURL = image_detailsJSON["prefix"] + str(i) + image_detailsJSON["suffix"]
        imageListStr.append(formImageURL)
    return imageListStr
register.filter('list_image_details_api3', list_image_details_api3)


# --------------------------- Return fist image from image_details of Api 3 ---------------------------
def first_image_details_api3(hotelId):
    strAPI3 = getHotelCardWHotelID(hotelId)
    # reference = "https://hotelapi.loyalty.dev/api/hotels/diH7

#     "image_details": {
#     "suffix": ".jpg",
#     "count": 56,
#     "prefix": "https://d2ey9sqrvkqdfs.cloudfront.net/diH7/"
#   },
    api3Response = requests.get(strAPI3).json()
    image_detailsJSON = api3Response["image_details"]
    imageStr = image_detailsJSON["prefix"] + "0" + image_detailsJSON["suffix"]
    imageStr = str(imageStr)
    return imageStr

register.filter('first_image_details_api3', first_image_details_api3)