import unittest
from unittest.mock import Mock
from pyonemap.core import OneMap

class TestOneMap(unittest.TestCase):
    def setUp(self):
        self.onemap = OneMap()

    def test_search(self):
        mock_response = {
            "results": [
                {
                    "SEARCHVAL": "5 Havelock Road",
                    "BLK_NO": "5",
                    "ROAD_NAME": "Havelock Road",
                    "POSTAL": "169610",
                    "X": "29068.100058874996",
                    "Y": "29357.549260427598",
                    "LATITUDE": "1.288576327",
                    "LONGITUDE": "103.83245770099999"
                }
            ]
        }

        self.onemap._make_request = Mock(return_value=mock_response)

        result = self.onemap.search("5 Havelock Road")
        self.assertEqual(result, mock_response["results"])

    def test_search(self):
        mock_response = {
            "results": {'GeocodeInfo': [{'BUILDINGNAME': 'NEW TOWN PRIMARY SCHOOL', 'BLOCK': '300', 'ROAD': 'TANGLIN HALT ROAD', 'POSTALCODE': '148812', 'XCOORD': '24303.3101027', 'YCOORD': '31333.3389857', 'LATITUDE': '1.2996418818103135', 'LONGITUDE': '103.80010216304007'}]}
        }

        self.onemap._make_request = Mock(return_value=mock_response)

        result = self.onemap.revGeoCodeXy(24291.97788882387, 31373.0117224489)
        self.assertEqual(result, mock_response["results"])

#{'GeocodeInfo': [{'BUILDINGNAME': 'KAMPONG UBI VIEW', 'BLOCK': '351', 'ROAD': 'UBI AVENUE 1', 'POSTALCODE': '400351', 'XCOORD': '35501.9607216', 'YCOORD': '34191.1578935', 'LATITUDE': '1.325486284730739', 'LONGITUDE': '103.90072773995409'}, {'BUILDINGNAME': 'KAMPONG UBI VIEW', 'BLOCK': '352', 'ROAD': 'UBI AVENUE 1', 'POSTALCODE': '400352', 'XCOORD': '35354.2225417', 'YCOORD': '34162.4855169', 'LATITUDE': '1.3252270180708603', 'LONGITUDE': '103.89940022649942'}, {'BUILDINGNAME': 'KAMPONG UBI VIEW', 'BLOCK': '349', 'ROAD': 'UBI AVENUE 1', 'POSTALCODE': '400349', 'XCOORD': '35485.6405577', 'YCOORD': '34228.9805541', 'LATITUDE': '1.3258283432645641', 'LONGITUDE': '103.90058110378057'}]}

if __name__ == "__main__":
    unittest.main()
