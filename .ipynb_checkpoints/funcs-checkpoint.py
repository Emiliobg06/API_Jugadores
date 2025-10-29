import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup as bs
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from urllib.parse import urljoin
import json


def equipo(team,id,slug):
    driver.get("https://www.sofascore.com/team/football/"+slug+"/"+str(id))
    cont1 = driver.page_source
    soup1 = bs(cont1)
    script_tag = soup1.find_all('script', {'type': 'application/ld+json'})
    x=script_tag[1]
    json_data = x.string
    data = json.loads(json_data)
    athletes = data.get('athlete', [])
    df = {'name':[i.get('name') for i in athletes], 'country':[i.get('nationality', {}).get('name') for i in athletes],'team':[team for i in athletes],'teamid':[id for i in athletes]}
    return df

def merge(dict1, dict2):
    # Merge dictionaries (concatenate lists)
    merged = {}
    for key in dict1:
        # Convert non-list values to single-item lists
        val1 = dict1[key] if isinstance(dict1[key], list) else [dict1[key]]
        val2 = dict2[key] if isinstance(dict2[key], list) else [dict2[key]]
        merged[key] = val1 + val2
    
    return merged