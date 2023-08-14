__author__ = "Teo Cheng Guan"
__copyright__ = "Copyright (C) 2023 Teo Cheng Guan"
__license__ = "MIT"

import requests
import os
from datetime import datetime
from .core import Core

class PlanningArea:
    def __init__(self, api_key=None):
        self.__core = Core(api_key)

    '''
        year string Optional. 
        If not specified, the latest data will be provided. Else, values available are 1998, 2008, 2014, and 2019.
    '''
    def getAllPlanningarea(self, year):
        endpoint = f"/api/public/popapi/getAllPlanningarea"
        params = {"year": year}
        response = self.__core.make_request(endpoint, params)
        return response

    '''
        year string Optional. 
        If not specified, the latest data will be provided. Else, values available are 1998, 2008, 2014, and 2019.
    '''
    def getPlanningareaNames(self, year):
        endpoint = f"/api/public/popapi/getPlanningareaNames"
        params = {"year": year}
        response = self.__core.make_request(endpoint, params)
        return response

    '''
        latitude string REQUIRED
        This represents the latitude of the point.

        longitude string REQUIRED
        This represents the longitude of the point.

        year string Optional. 
        If not specified, the latest data will be provided. Else, values available are 1998, 2008, 2014, and 2019.
    '''
    def getPlanningArea(self, lat, lon, year):
        endpoint = f"/api/public/popapi/getPlanningArea"
        params = {"lat": lat, "lon": lon, "year": year}
        response = self.__core.make_request(endpoint, params)
        return response

if __name__ == "__main__":
    pass