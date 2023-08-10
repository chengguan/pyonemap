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
