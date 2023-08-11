__author__ = "Teo Cheng Guan"
__copyright__ = "Copyright (C) 2023 Teo Cheng Guan"
__license__ = "MIT"

import requests
import os
from datetime import datetime
from core import Core

class Converter:
    def __init__(self, api_key=None):
        self.__core = Core(api_key)

    '''
        latitude string REQUIRED
        Latitude coordinates in WGS84 format.

        longitude string REQUIRED
        Longitude coordinates in WGS84 format.
    '''
    def convert4326to3857(self, lat, lon):
        endpoint = f"/api/common/convert/4326to3857"
        params = {"latitude": lat, "longitude": lon}
        response = self.__core.make_request(endpoint, params)
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
        response = self.__core.make_request(endpoint, params)
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
        response = self.__core.make_request(endpoint, params)
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
        response = self.__core.make_request(endpoint, params)
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
        response = self.__core.make_request(endpoint, params)
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
        response = self.__core.make_request(endpoint, params)
        return response

if __name__ == "__main__":
    pass