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
