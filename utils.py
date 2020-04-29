import requests

powerSrc = {
    "水力": 1,
    "汽力": 2,
    "ガスタービン": 3,
    "内燃力": 4,
    "火力計": 5,
    "原子力": 6,
    "新エネルギー等": 7,
    "その他": 8,
    "合計": 9
}

# kens of japan
chiho = {
    "hokkaido":"01",
    "tohuku":"02",
    "tokyo":"03",
    "chubu":"04",
    "hokuriku":"05",
    "kansai":"06",
    "chugoku":"07",
    "shikoku":"08",
    "kyushu":"09",
    "9社計":"10",
    "okinawa":"11",
    "10社計":"12"
}

'''
Returns a substring of the year (number only)
'''
def getYear(cell):
    year = cell[:4]
    return str(year)

'''
Returns status code of http request to url
'''
def testEndpoint(url):
    '''
    施設
    by company
    Hokkaido
    1963
    2020
    ki: Y
    jiku: ki
    '''
    testPost = {
        "item": "B11:1:",
        "ttl": "cmp",
        "cmp": "01",
        "nenFrom": 1963,
        "nenTo": 2020,
        "ki": "Y",
        "jiku": "ki"
    }
    response = requests.post(url, testPost)
    return response.text