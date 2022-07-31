from .models import DestinationCat


# # Default values
# checkin = "2022-08-20"
# checkout = "2022-08-22"
# guests = "2"

# -------------------------- API 1 --------------------------
def getAllHotelsPricesWDest(destId, checkin, checkout, guests):
    # reference = "https://hotelapi.loyalty.dev/api/hotels/prices?destination_id=WD0M&checkin=2022-08-20&checkout=2022-08-22&lang=en_US&currency=SGD&country_code=SG&guests=2&partner_id=1"
    
    # default values
    langStr = "en_US"
    currencyStr = "SGD"
    country_code= "SG"
    
    baseJSONStr = "https://hotelapi.loyalty.dev/api/hotels/prices?destination_id="
    getAllHotelsPricesWDestJSON = baseJSONStr + destId + "&checkin=" + checkin + "&checkout=" + checkout + "&lang=" + langStr + "&currency=" + currencyStr + "&country_code=" + country_code + "&guests=" + guests + "&partner_id=1"

    return str(getAllHotelsPricesWDestJSON)

# -------------------------- API 2 --------------------------
def getSingleHotelRoomTypes(hotelId, destId, checkin, checkout, guests):
    # reference = https://hotelapi.loyalty.dev/api/hotels/diH7/price?destination_id=WD0M&checkin=2022-08-20&checkout=2022-08-22&lang=en_US&currency=SGD&country_code=SG&guests=2&partner_id=1
    
    # default values
    langStr = "en_US"
    currencyStr = "SGD"
    country_code= "SG"

    baseJSONStr = "https://hotelapi.loyalty.dev/api/hotels/"
    getSingleHotelRoomTypesJSON = baseJSONStr  + hotelId + "/price?destination_id=" + destId + "&checkin=" + checkin + "&checkout=" + checkout + "&lang=" + langStr + "&currency=" + currencyStr + "&country_code=" + country_code + "&guests=" + guests + "&partner_id=1"
    
    return str(getSingleHotelRoomTypesJSON)

# -------------------------- API 3 --------------------------
def getHotelCardWHotelID(hotelId):
    # reference = "https://hotelapi.loyalty.dev/api/hotels/diH7"
    
    baseJSONStr = "https://hotelapi.loyalty.dev/api/hotels/"
    getHotelCardWHotelIDJSON = baseJSONStr + hotelId

    return str(getHotelCardWHotelIDJSON)

# -------------------------- API 4 --------------------------
def getSingleHotelCardWHotelID(destId):
    #reference = "https://hotelapi.loyalty.dev/api/hotels?destination_id=RsBU"
    
    # default values
    langStr = "en_US"
    currencyStr = "SGD"
    country_code= "SG"

    baseJSONStr = "https://hotelapi.loyalty.dev/api/hotels?destination_id="
    getSingleHotelCardWHotelIDJSON = baseJSONStr + destId

    return str(getSingleHotelCardWHotelIDJSON)


# -------------------------- Convert dest.json 'term' into destId --------------------------
def convertTermToDestId(destinationOrHotel):
    # destId=Singapore+Science+Centre%2C+Singapore
    searchInputObj = DestinationCat.objects.get(term=destinationOrHotel)
    # print(searchInputObj)
    destId = searchInputObj.uid

    #  hotelnamevar = ListingItem.objects.get(name=hotelname)

    return destId
