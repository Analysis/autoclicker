import json
import requests
from lxml import html
import numpy as np
import matplotlib.pyplot as plt
import time

# shark, barrow tab, 
ITEMS = [385,19629]

def ge_price(item_id):
    api_url = 'https://api.rsbuddy.com/grandExchange?a=guidePrice&i=' + str(item_id)
    page = requests.get(api_url)
    tree = html.fromstring(page.content)
    item_json = tree.xpath('//body//text()')[0].split(':')
    overall = item_json[1][:-9]
    buying = item_json[2][:-17]
    buying_Q = item_json[3][:-10]
    selling = item_json[4][:-18]
    selling_Q = item_json[5][:-1]
    return (overall,buying,buying_Q,selling,selling_Q)

def main():
    a = open('test.txt', 'a')
    a.write('test test test')
    a.close()
    
main()
    