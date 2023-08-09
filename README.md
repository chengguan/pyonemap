# PyOneMap - Python Wrapper for SLA's OneMap API

PyOneMap is a Python package that provides a convenient and easy-to-use interface for interacting with the Singapore Land Authority's (SLA) OneMap API. With PyOneMap, you can retrieve various geospatial data and information from OneMap's services directly from your Python code.

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
onemap = OneMap()

# Get location details
location = onemap.search("5 Havelock Road")
print(location)

geocode = onemap.revGeoCodeXy(24291.97788882387, 31373.0117224489)
print(geocode)

geocode = onemap.revGeoCode(1.3254295, 103.9005321)
print(geocode)

```

## Source
https://github.com/chengguan/pyonemap

## Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
