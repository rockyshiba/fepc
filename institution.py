import requests
import utils
from bs4 import BeautifulSoup

institution_items = {
    "＊水力": {
        "code": "B11:1:",
        "powerSrc": utils.powerSrc["水力"]
    },
    "＊汽力": {
        "code": "B11:3:",
        "powerSrc": utils.powerSrc["汽力"]
    },
    "＊ガスタービン": {
        "code": "B11:4:",
        "powerSrc": utils.powerSrc["ガスタービン"]
    },
    "＊内燃力": {
        "code": "B11:5:",
        "powerSrc": utils.powerSrc["内燃力"]
    },
    "＊火力計": {
        "code": "B11:7:",
        "powerSrc": utils.powerSrc["火力計"]
    },
    "＊原子力": {
        "code": "B11:8:",
        "powerSrc": utils.powerSrc["原子力"]
    },
    "＊新エネルギー等": {
        "code": "B11:9:",
        "powerSrc": utils.powerSrc["新エネルギー等"]
    },
    "＊その他": {
        "code":"B11:A:",
        "powerSrc": utils.powerSrc["その他"]
    },
    # "＊合計": {
    #     "code":"B11:C:",
    #     "powerSrc": utils.powerSrc["合計"]
    # }
}

'''
Scrapes information from the 施設 page
creates sql file to insert rows into the power_equip_cmp table
'''
def scrapeInstitution(url, yearFrom, yearTo):
    insert_statement = "delete from power_equip_cmp;commit;"
    insert_obj = {
        "year": None,
        "units": None,
        "output": None,
        "chiho": None,
        "powerSrc": None
    }
    for i in institution_items:
        insert_obj["powerSrc"] = institution_items[i]["powerSrc"]
        for c in utils.chiho:
            insert_obj["chiho"] = utils.chiho[c]
            postData = {
                "item": institution_items[i]["code"],
                "ttl":"cmp",
                "cmp":utils.chiho[c],
                "nenFrom":yearFrom,
                "nenTo":yearTo,
                "ki":"Y",
                "jiku":"ki"
            }
            response = requests.post(url, postData)
            soup = BeautifulSoup(response.text, "lxml")
            rows = soup.findAll("tr")
            for r in rows:
                cells = r.findChildren("td")
                if len(cells) > 3 and (cells[0].text != ''):
                    insert_obj['year'] = utils.getYear(cells[0].text)
                    insert_obj['units'] = cells[2].text if cells[2].text != '' else 'NULL'
                    insert_obj['output'] = cells[3].text if cells[3].text != '' else 'NULL'

                    insert_statement += "insert into power_equip_cmp (subcategory , power_src , chiho , units , kw_output , " + '"year"' + ") values (1, {powerSrc}, '{chiho}', {units}, {output}, '{year}');".format(**insert_obj)
    sqlFile = open("institution.sql", "w")
    sqlFile.write(insert_statement + "commit;")
    return insert_statement

# scrapeInstitution("http://www5.fepc.or.jp/tok-bin/knOut.cgi", 1963, 2020)