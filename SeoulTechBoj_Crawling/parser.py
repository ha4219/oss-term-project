import requests
from bs4 import BeautifulSoup
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SeoulTechBoj_Crawling.settings")

import django

django.setup()

from parsed_data.models import JustUserName
from problem.models import Problem
from tag.models import Tag


def get_names_page_size(BASE_URL):
    res = requests.get(BASE_URL)
    html = res.text
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


def checkTag(tag):
    if Tag.objects.get(name=tag):
        return True
    else:
        return False


def handleTag(tag):
    if not checkTag(tag):
        try:
            Tag(name=tag).save()
            return tag
        except:
            print('tag error...')
    return None


def saveProblem(data):
    # tags = [Tag.objects.get(name=tag["key"]) for tag in data["tags"]]
    try:
        Problem.objects.create(problemId=data["problemId"], titleKo=data["titleKo"], isSolvable=data["isSolvable"],
                               acceptedUserCount=data["acceptedUserCount"], level=data["level"],
                               averageTries=data["averageTries"], tags=data['tagss'],
                               solved=False).save()
        # for tag in tags:
        #     print(tag)
        #     Problem.objects.get(problemId=data["problemId"]).tag.add(tag)
    except:
        print('not save...')


def getProblem(problemId):
    url = 'https://solved.ac/api/v3/problem/show?problemId=%d' % problemId
    try:
        res = requests.get(url)

        data = res.json()
        # handle tag
        tags = data["tags"]
        tagss = []
        for tag in tags:
            tmp = handleTag(tag["key"])
            if tmp:
                tagss.append(tmp)
        data['tagss'] = tagss
        saveProblem(data)
        return True
    except:
        print('%d is error...' % problemId)
        return False


def getNewProblemId():
    problemCntUrl = 'https://acmicpc.net/problem/added'
    res = requests.get(problemCntUrl)
    html = res.text
    soup = BeautifulSoup(html, 'html.parser')

    page = soup.select(
        '#problemset > tbody > tr:nth-child(1) >td.list_problem_id'
    )
    return int(page[0].text)


def getProblems():
    import time
    start = 5254
    end = getNewProblemId()
    for problemId in range(start, end + 1):
        time.sleep(1)
        print(problemId, getProblem(problemId))
    return

def getSolvedProblem(name):
    BASE_URL = 'https://solved.ac/api/v3/search/problem?query=solved_by:'
    url = BASE_URL + name
    res = requests.get(url)
    try:
        data = res.json()
        from math import ceil
        import time
        page = ceil(data["count"] / 100)
        print(name, page)
        ret = set()
        for i in range(1, page + 1):
            time.sleep(10)
            try:
                url = BASE_URL + name + '&page=' + str(i)
                res = requests.get(url)
                data = res.json()
                for item in data["items"]:
                    ret.add(item['problemId'])
            except:
                continue
        return ret
    except:
        print(res)
        return False



def getProblemByUsers():
    from problem.models import SolvedProblem
    for name in JustUserName.objects.all():
        ret = getSolvedProblem(name.name)
        for item in ret:
            SolvedProblem(problemId=item).save()
    return SolvedProblem.objects.all()

def reviseSolvedProblems():
    from tqdm import tqdm
    res = getProblemByUsers()
    print(res)
    for item in tqdm(res):
        try:
            obj = Problem.objects.get(problemId=item)
            obj.solved = True
            obj.save()

            print(item, 'is solved')
        except:
            print(item, 'is not saved problem')

def solvedRefresh():
    from problem.models import SolvedProblem
    for item in SolvedProblem.objects.all():
        try:
            obj = Problem.objects.get(problemId=item.problemId)
            obj.solved = True
            obj.save()

            print(item.problemId, 'is solved')
        except:
            print(item.problemId, 'is not saved problem')

def getNotSolvedProblemByLevel(level):
    from problem.models import Problem
    return Problem.objects.filter(level=level, solved=False)


def refreshProblemStatusByLevel():
    from problem.models import Problem, ProblemStatusByLevel

    for level in range(31):
        total = len(Problem.objects.filter(level=level))
        solved = len(Problem.objects.filter(level=level, solved=True))
        notSolved = total - solved
        ProblemStatusByLevel(level=level, total=total, solved=solved, notSolved=notSolved).save()

refreshProblemStatusByLevel()
