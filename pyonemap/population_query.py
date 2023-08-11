__author__ = "Teo Cheng Guan"
__copyright__ = "Copyright (C) 2023 Teo Cheng Guan"
__license__ = "MIT"
__version__ = "1.0"

import requests
import os
from datetime import datetime
from .core import Core

class PopulationQuery:
    def __init__(self, api_key=None):
        self.__core = Core(api_key)

if __name__ == "__main__":
    pass