import unittest
import os
from unittest.mock import Mock
from pyonemap.onemap import OneMap

class TestOneMap(unittest.TestCase):
    def setUp(self):
        access_token = os.environ.get("ONEMAP_TOKEN")
        self.onemap = OneMap(access_token)

    def test_search(self):
        mock_response = {'found': 1, 'totalNumPages': 1, 'pageNum': 1, 'results': [{'SEARCHVAL': '640 ROWELL ROAD SINGAPORE 200640', 'BLK_NO': '640', 'ROAD_NAME': 'ROWELL ROAD', 'BUILDING': 'NIL', 'ADDRESS': '640 ROWELL ROAD SINGAPORE 200640', 'POSTAL': '200640', 'X': '30381.1007417506', 'Y': '32195.1006872542', 'LATITUDE': '1.30743547948389', 'LONGITUDE': '103.854713903431'}]}
        result = self.onemap.search("200640")
        self.assertEqual(result, mock_response)

    def test_revGeoCodeXy(self):
        mock_response = {'GeocodeInfo': [{'BUILDINGNAME': 'NEW TOWN PRIMARY SCHOOL', 'BLOCK': '300', 'ROAD': 'TANGLIN HALT ROAD', 'POSTALCODE': '148812', 'XCOORD': '24303.3101027', 'YCOORD': '31333.3389857', 'LATITUDE': '1.2996418818103135', 'LONGITUDE': '103.80010216304007'}]}
        result = self.onemap.reverseGeocode.revGeoCodeXy(24291.97788882387, 31373.0117224489)
        self.assertEqual(result, mock_response)

if __name__ == "__main__":
    unittest.main()

