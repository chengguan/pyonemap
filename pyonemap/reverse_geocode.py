__author__ = "Teo Cheng Guan"
__copyright__ = "Copyright (C) 2023 Teo Cheng Guan"
__license__ = "MIT"

from core import Core

class ReverseGeocode:
    def __init__(self, api_key=None):
        self.__core = Core(api_key)

    '''
        location string
        Latitude and Longitude Coordinates in WGS84 format.

        buffer string Optional. 
        Values: 0-500 (in meters). Rounds up all buildings in a circumference from a point and search building add

        addressType string Optional. 
        Values: HDB or All. Allows users to define property types within the buffer/radius. If HDB is selected, result

        otherFeatures string Optional. 
        Values: Y or N. Allows uses the page to retrieve information on reservoirs, playgrounds, jetties, etc. Default is N.
    '''
    def revGeoCodeXy(self, x, y, buffer=40, addressType='All', otherFeatures='N'):
        endpoint = f"/api/public/revgeocodexy"

        params = {"location": f'{x},{y}', 
                  "buffer": buffer, 
                  "addressType": addressType, 
                  "otherFeatures": otherFeatures}

        response = self.__core.make_request(endpoint, params)
        
        return response

    '''
        location string
        Latitude and Longitude Coordinates in WGS84 format.

        buffer string Optional. 
        Values: 0-500 (in meters). Rounds up all buildings in a circumference from a point and search building add

        addressType string Optional. 
        Values: HDB or All. Allows users to define property types within the buffer/radius. If HDB is selected, result

        otherFeatures string Optional. 
        Values: Y or N. Allows uses the page to retrieve information on reservoirs, playgrounds, jetties, etc. Default is N.
    '''
    def revGeoCode(self, lat, lon, buffer=40, addressType='All', otherFeatures='N'):
        endpoint = f"/api/public/revgeocode"

        params = {"location": f'{lat},{lon}', 
                  "buffer": buffer, 
                  "addressType": addressType, 
                  "otherFeatures": otherFeatures}

        response = self.__core.make_request(endpoint, params)
        
        return response

if __name__ == "__main__":
    pass

