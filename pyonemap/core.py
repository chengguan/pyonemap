__author__ = "Teo Cheng Guan"
__copyright__ = "Copyright (C) 2023 Teo Cheng Guan"
__license__ = "MIT"
__version__ = "1.0"

import requests
import os
from datetime import datetime

class OneMap:
    def __init__(self, api_key=None):
        self.__base_url = "https://www.onemap.gov.sg"
        self.__api_key = api_key

    def setToken(self, access_token):
        self.__api_key = access_token

    def getToken(email, password):
        url = "https://www.onemap.gov.sg/api/auth/post/getToken"
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
        url = f"{self.__base_url}{endpoint}"
        headers = {}

        if self.__api_key:
            headers["Authorization"] = f"Bearer {self.__api_key}"

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

    '''
        start string REQUIRED
        The start point in WGS84 latitude, longitude format.

        end string REQUIRED
        The end point in WGS84 latitude, longitude format.

        routeType string REQUIRED
        Route types available pt (default), walk, drive and cycle. Only lowercase is allowed.

        date string REQUIRED
        Date of the selected start point in MM-DD-YYYY.

        time string REQUIRED
        Time of the selected start point in HH:MM:SS, using the 24-hour clock system. 
        [HH] refers to a zero-padded hour between 00 and 23. 
        [MM] refers to a zero-padded minute between 00 and 59. 
        [SS] refers to a zero-padded second between 00 and 59.

        mode string REQUIRED
        Mode of public transport: TRANSIT (default), BUS, RAIL. Entry must be specified in UPPERCASE

        maxWalkDistance string Optional. 
        The maximum walking distance set by the user in metres. Default is 1000m.

        numItineraries string Optional. 
        Limits the number of return results: 1 to 3.
    '''
    def route(self, start_lat, start_lon, end_lat, end_lon, 
                    routeType='pt', date='', time='', mode='TRANSIT', 
                    maxWalkDistance=1000, numItineraries=3):
        endpoint = f"/api/public/routingsvc/route"
        available_modes = ['TRANSIT', 'BUS', 'RAIL']
        
        if routeType == 'walk' or routeType == 'drive' or routeType == 'cycle':
            params = {"start": f'{start_lat},{start_lon}', 
                      "end": f'{end_lat},{end_lon}', 
                      "routeType": routeType}
        elif routeType == 'pt':
            if mode not in available_modes:
                print(f'Error: invalid mode of transport: {mode}.')
                return None

            # Fill up with the current date and time if the inputs are not given.
            now = datetime.now()
            if date == '':
                date = now.strftime('%m-%d-%Y')
            if time == '':
                time = now.strftime('%H:%M:%S')

            params = {"start": f'{start_lat},{start_lon}', 
                      "end": f'{end_lat},{end_lon}', 
                      "routeType": routeType, 
                      "date": date, 
                      "time": time,
                      "mode": mode,
                      "maxWalkDistance": maxWalkDistance,
                      "numItineraries": numItineraries}
        else:
            print(f'Error: invalid routeType: {routeType}.')
            return None

        response = self._make_request(endpoint, params)
        
        return response

    '''
        latitude string REQUIRED
        Latitude coordinates in WGS84 format.

        longitude string REQUIRED
        Longitude coordinates in WGS84 format.
    '''
    def convert4326to3857(self, lat, lon):
        endpoint = f"/api/common/convert/4326to3857"
        params = {"latitude": lat, "longitude": lon}
        response = self._make_request(endpoint, params)
        return response

    '''
        latitude string REQUIRED
        Latitude coordinates in WGS84 format.

        longitude string REQUIRED
        Longitude coordinates in WGS84 format.
    '''
    def convert4326to3414(self, lat, lon):
        endpoint = f"/api/common/convert/4326to3414"
        params = {"latitude": lat, "longitude": lon}
        response = self._make_request(endpoint, params)
        return response

    '''
        Y string REQUIRED
        Y coordinates in SVY21 format.

        X string REQUIRED
        X coordinates in SVY21 format.
    '''
    def convert3414to3857(self, x, y):
        endpoint = f"/api/common/convert/3414to3857"
        params = {"X": x, "Y": y}
        response = self._make_request(endpoint, params)
        return response

    '''
        Y string REQUIRED
        Y coordinates in SVY21 format.

        X string REQUIRED
        X coordinates in SVY21 format.
    '''
    def convert3414to4326(self, x, y):
        endpoint = f"/api/common/convert/3414to4326"
        params = {"X": x, "Y": y}
        response = self._make_request(endpoint, params)
        return response

    '''
        Y string REQUIRED
        Y coordinates in SVY21 format.

        X string REQUIRED
        X coordinates in SVY21 format.
    '''
    def convert3857to3414(self, y, x):
        endpoint = f"/api/common/convert/3857to3414"
        params = {"Y": y, "X": x}
        response = self._make_request(endpoint, params)
        return response

    '''
        Y string REQUIRED
        Y coordinates in SVY21 format.

        X string REQUIRED
        X coordinates in SVY21 format.
    '''
    def convert3857to4326(self, y, x):
        endpoint = f"/api/common/convert/3857to4326"
        params = {"Y": y, "X": x}
        response = self._make_request(endpoint, params)
        return response

if __name__ == "__main__":
    # Obtain the access token using email and password:
    response = OneMap.getToken('your_email@email.com', 'your_password')
    access_token = response['access_token']
    
    # Or, pre-set it as environmental variable:
    #access_token = os.environ.get("ONEMAP_TOKEN")

    onemap = OneMap(access_token)
    
    location = onemap.search("200640", 'Y', 'Y')
    print(location)
    # {'found': 1, 'totalNumPages': 1, 'pageNum': 1, 
    # 'results': [{'SEARCHVAL': '640 ROWELL ROAD SINGAPORE 200640', 
    #   'BLK_NO': '640', 'ROAD_NAME': 'ROWELL ROAD', 'BUILDING': 'NIL', 
    #   'ADDRESS': '640 ROWELL ROAD SINGAPORE 200640', 'POSTAL': '200640', 
    #   'X': '30381.1007417506', 'Y': '32195.1006872542', 
    #   'LATITUDE': '1.30743547948389', 'LONGITUDE': '103.854713903431'}]}

    geocode = onemap.revGeoCodeXy(24291.97788882387, 31373.0117224489)
    print(geocode)
    # {'GeocodeInfo': [{'BUILDINGNAME': 'NEW TOWN PRIMARY SCHOOL', 
    #       'BLOCK': '300', 'ROAD': 'TANGLIN HALT ROAD', 'POSTALCODE': '148812', 
    #       'XCOORD': '24303.3101027', 'YCOORD': '31333.3389857', 
    #       'LATITUDE': '1.2996418818103135', 'LONGITUDE': '103.80010216304007'}]}

    geocode = onemap.revGeoCode(1.3254295, 103.9005321)
    print(geocode)
    # {'GeocodeInfo': [{'BUILDINGNAME': 'KAMPONG UBI VIEW', 
    #       'BLOCK': '351', 'ROAD': 'UBI AVENUE 1', 'POSTALCODE': '400351', 
    #       'XCOORD': '35501.9607216', 'YCOORD': '34191.1578935', 
    #       'LATITUDE': '1.325486284730739', 'LONGITUDE': '103.90072773995409'}, 
    #       {'BUILDINGNAME': 'KAMPONG UBI VIEW', 
    #       'BLOCK': '352', 'ROAD': 'UBI AVENUE 1', 'POSTALCODE': '400352', 
    #       'XCOORD': '35354.2225417', 'YCOORD': '34162.4855169', 
    #       'LATITUDE': '1.3252270180708603', 'LONGITUDE': '103.89940022649942'}, 
    #       {'BUILDINGNAME': 'KAMPONG UBI VIEW', 
    #       'BLOCK': '349', 'ROAD': 'UBI AVENUE 1', 'POSTALCODE': '400349', 
    #       'XCOORD': '35485.6405577', 'YCOORD': '34228.9805541', 
    #       'LATITUDE': '1.3258283432645641', 'LONGITUDE': '103.90058110378057'}]}

    route = onemap.route(1.320981, 103.844150, 1.326762, 103.8559)
    print(route)

    coordinate = onemap.convert4326to3857(1.319728905, 103.8421581)
    print(coordinate)
    # {'Y': 146924.54200324757, 'X': 11559656.16256661}
    
    coordinate = onemap.convert4326to3414(1.319728905, 103.8421581)
    print(coordinate)
    # {'Y': 33554.4360965479, 'X': 28983.75169436287}

    coordinate = onemap.convert3414to3857(28983.788791079794, 33554.509813284)
    print(coordinate)
    # {'Y': 146924.61623595929, 'X': 11559656.199673364}

    coordinate = onemap.convert3414to4326(28983.788791079794, 33554.5098132845)
    print(coordinate)
    # {'latitude': 1.3197295716669164, 'longitude': 103.84215843333567}

    coordinate = onemap.convert3857to3414(146924.54200324757, 11559656.16256661)
    print(coordinate)
    # {'Y': 33554.4360965483, 'X': 28983.75169436287}

    coordinate = onemap.convert3857to4326(146924.54200324757, 11559656.16256661)
    print(coordinate)
    # {'latitude': 1.3197289050000036, 'longitude': 103.8421581}