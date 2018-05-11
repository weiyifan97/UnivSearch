# Get all universities worldwide from http://univ.cc/
import requests
from bs4 import BeautifulSoup as bs

url = 'http://univ.cc/search.php'

univs = []

def getUniv(dom, maxim):
    start = 1   # increment is 50

    while start < maxim:
        respond = requests.get(url+'?dom={}&key=&start={}'.format(dom, start))
        soup = bs(respond.content, 'html.parser')
        ol = soup.find('body').find('div', id='content').find('table').find('tr').find('td').find('ol')
        # ol = soup.body.div.table.tr.td.ol
        for li in ol:
            a = li.find('a')
            for child in a.children:
                univs.append(child.string)

        print('page {} cleared!'.format((start-1)//50))

        start += 50

    print('All', dom, 'cleared !')

# Except US
getUniv('world', 7495)

# In the US
getUniv('edu', 2064)

with open('data/Universities', 'w') as out:
    for univ in univs:
        out.write(univ)
        out.write('\n')
