__author__ = "Teo Cheng Guan"
__copyright__ = "Copyright (C) 2023 Teo Cheng Guan"
__license__ = "MIT"
__version__ = "1.0"

import requests
import os

class OneMap:
    def __init__(self, api_key=None):
        self.base_url = "https://www.onemap.gov.sg"
        self.api_key = api_key

    def getToken(self, email, password):
        url = f"{self.base_url}/api/auth/post/getToken"
        payload = {"email": email, "password": password}

        try:
            response = requests.request("POST", url, json=payload)
            response.raise_for_status()  # Check for HTTP errors
        except requests.exceptions.RequestException as e:
            # Handle any exceptions that occurred during the request
            print(f"An error occurred: {e}")
            return None
        
        return response.json()

    def _make_request(self, endpoint, params):
        url = f"{self.base_url}{endpoint}"
        headers = {}

        if self.api_key:
            headers["Authorization"] = f"Bearer {self.api_key}"

        response = requests.get(url, params=params, headers=headers)

        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()

    '''
        searchVal string REQUIRED
        Keywords entered by users to filter the results

        returnGeom string REQUIRED
        Values: Y, N . Enter Y if user wants the geometry value returned.

        getAddrDetails string REQUIRED
        Values: Y, N . Enter Y if user wants address details returned.

        pageNum integer Optional. 
        Specifies the page to retrieve search results.

    '''
    def search(self, searchVal, returnGeom='Y', getAddressDetails='Y', pageNum=1):
        endpoint = f"/api/common/elastic/search"
        params = {"searchVal": searchVal, 
                  "returnGeom": returnGeom, 
                  "getAddrDetails": getAddressDetails, 
                  "pageNum": pageNum}

        response = self._make_request(endpoint, params)
        return response.get("results", [])

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

        response = self._make_request(endpoint, params)
        
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

        response = self._make_request(endpoint, params)
        
        return response


if __name__ == "__main__":
    onemap = OneMap()
    
    location = onemap.search("5 Havelock Road", 'Y', 'Y')
    print(location)

    geocode = onemap.revGeoCodeXy(24291.97788882387, 31373.0117224489)
    print(geocode)

    geocode = onemap.revGeoCode(1.3254295, 103.9005321)
    print(geocode)