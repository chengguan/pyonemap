__author__ = "Teo Cheng Guan"
__copyright__ = "Copyright (C) 2023 Teo Cheng Guan"
__license__ = "MIT"

import requests

class Core:
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

    def make_request(self, endpoint, params):
        url = f"{self.__base_url}{endpoint}"
        headers = {}

        if self.__api_key:
            headers["Authorization"] = f"Bearer {self.__api_key}"

        response = requests.get(url, params=params, headers=headers)

        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()

if __name__ == "__main__":
    pass