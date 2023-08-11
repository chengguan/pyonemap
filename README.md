# PyOneMap - Python Wrapper for SLA's OneMap API

PyOneMap is a Python package that provides a convenient and easy-to-use interface for interacting with the Singapore Land Authority's (SLA) OneMap API. With PyOneMap, you can retrieve various geospatial data and information from OneMap's services directly from your Python code.

This is built using the [API doc](https://www.onemap.gov.sg/apidocs/apidocs) release in 2023. The old API documentation and APIs will be available until 31 August 2023.

## Features

- Retrieve location details such as addresses, postal codes, and coordinates.
- Search for places of interest, amenities, and landmarks in Singapore.
- Perform geocoding and reverse geocoding operations effortlessly.
- Access map layers and thematic data provided by the OneMap API.

## Installation

You can install PyOneMap using pip:

```bash
pip install pyonemap
```

## Usage

```python
from pyonemap import OneMap

# Initialize the OneMapAPI client
onemap = OneMap('<--Insert your OneMap API token here-->')

# Get location details
location = onemap.search("5 Havelock Road")
print(location)

geocode = onemap.revGeoCodeXy(24291.97788882387, 31373.0117224489)
print(geocode)

geocode = onemap.revGeoCode(1.3254295, 103.9005321)
print(geocode)

```

## Example
```python
    access_token = os.environ.get("ONEMAP_TOKEN")

    onemap = OneMap(access_token)
    
    location = onemap.search("200640", 'Y', 'Y')
    print(location)
    # {'found': 1, 'totalNumPages': 1, 'pageNum': 1, 
    # 'results': [{'SEARCHVAL': '640 ROWELL ROAD SINGAPORE 200640', 
    #   'BLK_NO': '640', 'ROAD_NAME': 'ROWELL ROAD', 'BUILDING': 'NIL', 
    #   'ADDRESS': '640 ROWELL ROAD SINGAPORE 200640', 'POSTAL': '200640', 
    #   'X': '30381.1007417506', 'Y': '32195.1006872542', 
    #   'LATITUDE': '1.30743547948389', 'LONGITUDE': '103.854713903431'}]}

    geocode = onemap.reverseGeocode.revGeoCodeXy(24291.97788882387, 31373.0117224489)
    print(geocode)
    # {'GeocodeInfo': [{'BUILDINGNAME': 'NEW TOWN PRIMARY SCHOOL', 
    #       'BLOCK': '300', 'ROAD': 'TANGLIN HALT ROAD', 'POSTALCODE': '148812', 
    #       'XCOORD': '24303.3101027', 'YCOORD': '31333.3389857', 
    #       'LATITUDE': '1.2996418818103135', 'LONGITUDE': '103.80010216304007'}]}

    geocode = onemap.reverseGeocode.revGeoCode(1.3254295, 103.9005321)
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

    route = onemap.routing.route(1.320981, 103.844150, 1.326762, 103.8559)
    print(route['requestParameters']['preferredRoutes'])

    coordinate = onemap.converter.convert4326to3857(1.319728905, 103.8421581)
    print(coordinate)
    # {'Y': 146924.54200324757, 'X': 11559656.16256661}
    
    coordinate = onemap.converter.convert4326to3414(1.319728905, 103.8421581)
    print(coordinate)
    # {'Y': 33554.4360965479, 'X': 28983.75169436287}

    coordinate = onemap.converter.convert3414to3857(28983.788791079794, 33554.509813284)
    print(coordinate)
    # {'Y': 146924.61623595929, 'X': 11559656.199673364}

    coordinate = onemap.converter.convert3414to4326(28983.788791079794, 33554.5098132845)
    print(coordinate)
    # {'latitude': 1.3197295716669164, 'longitude': 103.84215843333567}

    coordinate = onemap.converter.convert3857to3414(146924.54200324757, 11559656.16256661)
    print(coordinate)
    # {'Y': 33554.4360965483, 'X': 28983.75169436287}

    coordinate = onemap.converter.convert3857to4326(146924.54200324757, 11559656.16256661)
    print(coordinate)
    # {'latitude': 1.3197289050000036, 'longitude': 103.8421581}

    themeStatus = onemap.themes.checkThemeStatus('kindergartens')
    print(themeStatus)
    # {'UpdatedFile': True}

    themeInfo = onemap.themes.getThemeInfo('kindergartens')
    print(themeInfo)
    # {'Theme_Names': [{'THEMENAME': 'Kindergartens', 'QUERYNAME': 'kindergartens'}]}

    allThemes = onemap.themes.getAllThemesInfo()
    print(f'Found {len(allThemes["Theme_Names"])} themes.')
    # {'Theme_Names': [{'THEMENAME': 'Kindergartens', 'QUERYNAME': 'kindergartens'}]}

    searchTheme = 'dengue_cluster'
    theme = onemap.themes.retrieveTheme(searchTheme)
    print(f'{len(theme["SrchResults"])} of {searchTheme} found.')
    # {'SrchResults': [{'FeatCount': 37, 'Theme_Name': 'Dengue Clusters', 'Category': 'Health', 'Owner': 'NATION ...

    boundary = '1.291789%2C103.7796402%2C1.3290461%2C103.8726032'
    exTheme = onemap.themes.retrieveTheme(searchTheme, boundary)
    print(f'{len(theme["SrchResults"])} of {searchTheme} found (with boundaries).')
    # {'SrchResults': [{'FeatCount': 37, 'Theme_Name': 'Dengue Clusters', 'Category': 'Health', 'Owner': 'NATION ...

    year = '2019'
    allPlanningArea = onemap.planningArea.getAllPlanningarea(year)
    print(f'{len(allPlanningArea["SearchResults"])} planning areas found for the year {year}.')

    planningAreaNames = onemap.planningArea.getPlanningareaNames(year)
    print(f'{len(planningAreaNames)} planning area names found for the year {year}.')

    lat = 1.3
    lon = 103.8
    planningArea = onemap.planningArea.getPlanningArea(lat, lon, year)
    print(f'({lat}, {lon}) is located in planning area {planningArea[0]["pln_area_n"]} in the year of {year}.')

    print(onemap.populationQuery.getEconomicStatus("Bedok", 2010))
    print(onemap.populationQuery.getEducationAttending("Bedok", 2020))
    print(onemap.populationQuery.getEthnicGroup("Bedok", 2020))
    print(onemap.populationQuery.getHouseholdMonthlyIncomeWork("Bedok", 2020))
    print(onemap.populationQuery.getHouseholdSize("Bedok", 2020))
    print(onemap.populationQuery.getHouseholdStructure("Bedok", 2020))
    print(onemap.populationQuery.getIncomeFromWork("Bedok", 2020))
    print(onemap.populationQuery.getIndustry("Bedok", 2020))
    print(onemap.populationQuery.getLanguageLiterate("Bedok", 2020))
    print(onemap.populationQuery.getMaritalStatus("Bedok", 2020))
    print(onemap.populationQuery.getModeOfTransportSchool("Bedok", 2020))
    print(onemap.populationQuery.getModeOfTransportWork("Bedok", 2020))
    print(onemap.populationQuery.getPopulationAgeGroup("Bedok", 2020))
    print(onemap.populationQuery.getReligion("Bedok", 2020))
    print(onemap.populationQuery.getSpokenAtHome("Bedok", 2020))
    print(onemap.populationQuery.getTenancy("Bedok", 2020))
    print(onemap.populationQuery.getTypeOfDwellingHousehold("Bedok", 2020))
    print(onemap.populationQuery.getTypeOfDwellingPop("Bedok", 2020))
```

## Unit Test

```python
python3 -m unittest discover -s tests -p "test_*.py"
```

## Building and Uploading

```
$ python3 setup.py sdist bdist_wheel
$ twine upload ./dist/*
```

## Source
https://github.com/chengguan/pyonemap

## Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
