__author__ = "Teo Cheng Guan"
__copyright__ = "Copyright (C) 2023 Teo Cheng Guan"
__license__ = "MIT"

import requests
import os
from datetime import datetime
from core import Core

class Themes:
    def __init__(self, api_key=None):
        self.__core = Core(api_key)

    '''
        queryName string REQUIRED
        Query name. Themes’ query names can be retrieved using Get All Themes Info service.

        dateTime string REQUIRED
        The datetime in YYYY-MM-DDTHH:MM:SS:FFFZ. EG: 2023-06-15T16:00:00.000Z format.
    '''
    def checkThemeStatus(self, queryName, dateTime=''):
        endpoint = f"/api/public/themesvc/checkThemeStatus"

        if dateTime == '':
            now = datetime.now()
            dateTime = now.strftime('YYYY-MM-DDTHH:MM:SS:FFFZ')

        params = {"queryName": queryName, "dateTime": dateTime}
        response = self.__core.make_request(endpoint, params)
        return response

    '''
        queryName string REQUIRED
        Enables users to retrieve theme information. Themes' query names can be retrieved using Get All Themes Info service.
    '''
    def getThemeInfo(self, queryName):
        endpoint = f"/api/public/themesvc/getThemeInfo"
        params = {"queryName": queryName}
        response = self.__core.make_request(endpoint, params)
        return response

    '''
        moreInfo string
        Optional. Values: Y, N. Returns more information of themes such as icon names, category names, and theme owners if set as Y. 
        Default is N.
    '''
    def getAllThemesInfo(self, moreInfo='N'):
        endpoint = f"/api/public/themesvc/getAllThemesInfo"
        params = {"moreInfo": moreInfo}
        response = self.__core.make_request(endpoint, params)
        return response

    '''
        queryName string REQUIRED
        Enables users to retrieve theme information. Themes' query names can be retrieved using Get All Themes Info service.
        
        extents string Optional. 
        Boundary provided by user. EG: 1.291789,103.7796402,1.3290461,103.8726032
    '''
    def retrieveTheme(self, queryName, extents=''):
        endpoint = f"/api/public/themesvc/retrieveTheme"
        if extents == '':
            params = {"queryName": queryName}
        else:
            params = {"queryName": queryName, "extents": extents}
        response = self.__core.make_request(endpoint, params)
        return response

if __name__ == "__main__":
    pass

