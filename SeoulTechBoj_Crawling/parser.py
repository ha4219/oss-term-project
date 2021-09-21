import requests
from bs4 import BeautifulSoup
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SeoulTechBoj_Crawling.settings")

import django

django.setup()

from parsed_data.models import JustUserName


def get_names_page_size(BASE_URL):
    request = requests.get(BASE_URL)
    html = request.text
    soup = BeautifulSoup(html, 'html.parser')

    # check page size
    page = soup.select(
        'body > div.wrapper > div.container.content > div.row > div:nth-child(4) > div > ul > li'
    )
    page_size = len(page) - 2
    return page_size


def get_names():
    BASE_URL = 'https://www.acmicpc.net/school/ranklist/295'

    page_size = get_names_page_size(BASE_URL)
    res = set()
    for i in range(1, page_size + 1):
        request = requests.get('%s/%d' % (BASE_URL, i))
        html = request.text
        soup = BeautifulSoup(html, 'html.parser')

        data = soup.select(
            '#ranklist > tbody > tr > td:nth-child(2) > a'
        )
        for dat in data:
            res.add(dat.text)
    for name in res:
        try:
            JustUserName(name=name).save()
        except:
            print('%s was in data' % name)
    return len(res)

def getSolvedProblem(name):
    import json
    BASE_URL = 'https://solved.ac/api/v3/search/problem?query=solved_by:'
    url = BASE_URL + name
    res = requests.get(url)

    data = res.json()
    print(data["count"])
    print(len(data["items"]))
    return res

print(getSolvedProblem('jeongdongha'))
