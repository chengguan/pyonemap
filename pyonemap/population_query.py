__author__ = "Teo Cheng Guan"
__copyright__ = "Copyright (C) 2023 Teo Cheng Guan"
__license__ = "MIT"

import requests
import os
from datetime import datetime
from core import Core

class PopulationQuery:
    def __init__(self, api_key=None):
        self.__core = Core(api_key)

    '''
        planningArea string REQUIRED 
        Planning area name can be retrieved from "Names of planning area".

        year string REQUIRED
        Years available are 2000, 2010, 2015, and 2020.

        gender string Optional. 
        Male or female, returns all results by default.
    '''
    def getEconomicStatus(self, planningArea, year, gender=''):
        endpoint = f"/api/public/popapi/getEconomicStatus"
        if gender != '':
            params = {"planningArea": planningArea, "year": year, "gender": gender}
        else:
            params = {"planningArea": planningArea, "year": year}
        response = self.__core.make_request(endpoint, params)
        return response

    '''
        planningArea string REQUIRED 
        Planning area name can be retrieved from "Names of planning area".

        year string REQUIRED
        Years available are 2000, 2010, 2015, and 2020.
    '''
    def getEducationAttending(self, planningArea, year):
        endpoint = f"/api/public/popapi/getEducationAttending"
        params = {"planningArea": planningArea, "year": year}
        response = self.__core.make_request(endpoint, params)
        return response

    '''
        planningArea string REQUIRED 
        Planning area name can be retrieved from "Names of planning area".

        year string REQUIRED
        Years available are 2000, 2010, 2015, and 2020.

        gender string Optional. 
        Male or female, returns all results by default.
    '''
    def getEthnicGroup(self, planningArea, year, gender=''):
        endpoint = f"/api/public/popapi/getEthnicGroup"
        if gender != '':
            params = {"planningArea": planningArea, "year": year, "gender": gender}
        else:
            params = {"planningArea": planningArea, "year": year}
        response = self.__core.make_request(endpoint, params)
        return response

    '''
        planningArea string REQUIRED 
        Planning area name can be retrieved from "Names of planning area".

        year string REQUIRED
        Years available are 2000, 2010, 2015, and 2020.
    '''
    def getHouseholdMonthlyIncomeWork(self, planningArea, year):
        endpoint = f"/api/public/popapi/getHouseholdMonthlyIncomeWork"
        params = {"planningArea": planningArea, "year": year}
        response = self.__core.make_request(endpoint, params)
        return response

    '''
        planningArea string REQUIRED 
        Planning area name can be retrieved from "Names of planning area".

        year string REQUIRED
        Years available are 2000, 2010, 2015, and 2020.
    '''
    def getHouseholdSize(self, planningArea, year):
        endpoint = f"/api/public/popapi/getHouseholdSize"
        params = {"planningArea": planningArea, "year": year}
        response = self.__core.make_request(endpoint, params)
        return response

    '''
        planningArea string REQUIRED 
        Planning area name can be retrieved from "Names of planning area".

        year string REQUIRED
        Years available are 2000, 2010, 2015, and 2020.
    '''
    def getHouseholdStructure(self, planningArea, year):
        endpoint = f"/api/public/popapi/getHouseholdStructure"
        params = {"planningArea": planningArea, "year": year}
        response = self.__core.make_request(endpoint, params)
        return response

    '''
        planningArea string REQUIRED 
        Planning area name can be retrieved from "Names of planning area".

        year string REQUIRED
        Years available are 2000, 2010, 2015, and 2020.
    '''
    def getIncomeFromWork(self, planningArea, year):
        endpoint = f"/api/public/popapi/getIncomeFromWork"
        params = {"planningArea": planningArea, "year": year}
        response = self.__core.make_request(endpoint, params)
        return response

    '''
        planningArea string REQUIRED 
        Planning area name can be retrieved from "Names of planning area".

        year string REQUIRED
        Years available are 2000, 2010, 2015, and 2020.
    '''
    def getIndustry(self, planningArea, year):
        endpoint = f"/api/public/popapi/getIndustry"
        params = {"planningArea": planningArea, "year": year}
        response = self.__core.make_request(endpoint, params)
        return response

    '''
        planningArea string REQUIRED 
        Planning area name can be retrieved from "Names of planning area".

        year string REQUIRED
        Years available are 2000, 2010, 2015, and 2020.
    '''
    def getLanguageLiterate(self, planningArea, year):
        endpoint = f"/api/public/popapi/getLanguageLiterate"
        params = {"planningArea": planningArea, "year": year}
        response = self.__core.make_request(endpoint, params)
        return response

    '''
        planningArea string REQUIRED 
        Planning area name can be retrieved from "Names of planning area".

        year string REQUIRED
        Years available are 2000, 2010, 2015, and 2020.

        gender string Optional. 
        Male or female, returns all results by default.
    '''
    def getMaritalStatus(self, planningArea, year, gender=''):
        endpoint = f"/api/public/popapi/getMaritalStatus"
        if gender != '':
            params = {"planningArea": planningArea, "year": year, "gender": gender}
        else:
            params = {"planningArea": planningArea, "year": year}
        response = self.__core.make_request(endpoint, params)
        return response

    '''
        planningArea string REQUIRED 
        Planning area name can be retrieved from "Names of planning area".

        year string REQUIRED
        Years available are 2000, 2010, 2015, and 2020.
    '''
    def getModeOfTransportSchool(self, planningArea, year):
        endpoint = f"/api/public/popapi/getModeOfTransportSchool"
        params = {"planningArea": planningArea, "year": year}
        response = self.__core.make_request(endpoint, params)
        return response

    '''
        planningArea string REQUIRED 
        Planning area name can be retrieved from "Names of planning area".

        year string REQUIRED
        Years available are 2000, 2010, 2015, and 2020.
    '''
    def getModeOfTransportWork(self, planningArea, year):
        endpoint = f"/api/public/popapi/getModeOfTransportWork"
        params = {"planningArea": planningArea, "year": year}
        response = self.__core.make_request(endpoint, params)
        return response

    '''
        planningArea string REQUIRED 
        Planning area name can be retrieved from "Names of planning area".

        year string REQUIRED
        Years available are 2000, 2010, 2015, and 2020.

        gender string Optional. 
        Male or female, returns all results by default.
    '''
    def getPopulationAgeGroup(self, planningArea, year, gender=''):
        endpoint = f"/api/public/popapi/getPopulationAgeGroup"
        if gender != '':
            params = {"planningArea": planningArea, "year": year, "gender": gender}
        else:
            params = {"planningArea": planningArea, "year": year}
        response = self.__core.make_request(endpoint, params)
        return response

    '''
        planningArea string REQUIRED 
        Planning area name can be retrieved from "Names of planning area".

        year string REQUIRED
        Years available are 2000, 2010, 2015, and 2020.
    '''
    def getReligion(self, planningArea, year):
        endpoint = f"/api/public/popapi/getReligion"
        params = {"planningArea": planningArea, "year": year}
        response = self.__core.make_request(endpoint, params)
        return response

    '''
        planningArea string REQUIRED 
        Planning area name can be retrieved from "Names of planning area".

        year string REQUIRED
        Years available are 2000, 2010, 2015, and 2020.
    '''
    def getSpokenAtHome(self, planningArea, year):
        endpoint = f"/api/public/popapi/getSpokenAtHome"
        params = {"planningArea": planningArea, "year": year}
        response = self.__core.make_request(endpoint, params)
        return response

    '''
        planningArea string REQUIRED 
        Planning area name can be retrieved from "Names of planning area".

        year string REQUIRED
        Years available are 2000, 2010, 2015, and 2020.
    '''
    def getTenancy(self, planningArea, year):
        endpoint = f"/api/public/popapi/getTenancy"
        params = {"planningArea": planningArea, "year": year}
        response = self.__core.make_request(endpoint, params)
        return response

    '''
        planningArea string REQUIRED 
        Planning area name can be retrieved from "Names of planning area".

        year string REQUIRED
        Years available are 2000, 2010, 2015, and 2020.
    '''
    def getTypeOfDwellingHousehold(self, planningArea, year):
        endpoint = f"/api/public/popapi/getTypeOfDwellingHousehold"
        params = {"planningArea": planningArea, "year": year}
        response = self.__core.make_request(endpoint, params)
        return response

    '''
        planningArea string REQUIRED 
        Planning area name can be retrieved from "Names of planning area".

        year string REQUIRED
        Years available are 2000, 2010, 2015, and 2020.
    '''
    def getTypeOfDwellingPop(self, planningArea, year):
        endpoint = f"/api/public/popapi/getTypeOfDwellingPop"
        params = {"planningArea": planningArea, "year": year}
        response = self.__core.make_request(endpoint, params)
        return response
        
if __name__ == "__main__":
    pass

