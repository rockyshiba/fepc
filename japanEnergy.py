import requests
import time
import urllib.request
from bs4 import BeautifulSoup

import utils

# categories
import institution

# Send post request to url with data
url = "http://www5.fepc.or.jp/tok-bin/knOut.cgi"

# print(utils.testEndpoint(url))

institution.scrapeInstitution(url, 1963, 2020)
