__author__ = "Teo Cheng Guan"
__copyright__ = "Copyright (C) 2023 Teo Cheng Guan"
__license__ = "MIT"
__version__ = "1.0"

import requests
import os
from datetime import datetime
from .core import Core

class Routing:
    def __init__(self, api_key=None):
        self.__core = Core(api_key)

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

        response = self.__core.make_request(endpoint, params)
        
        return response

if __name__ == "__main__":
    pass

