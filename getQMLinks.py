# Using HN Search to search for all Quanta Magazine articles and get links
import requests

url = 'http://hn.algolia.com/api/v1/search_by_date'

links = []

# At the current time, the maxim number of page is 46
page = 0
while True:
    keys = {
        'query' : 'quantamagazine.org',
        'tags'  : 'story',
        'page'  : page
    }

    respond = requests.get(url, data=keys).json()

    if len(respond['hits']) == 0:
        break

    for link in respond['hits']:
        if link['url'] != None and link['url'][:30] == 'https://www.quantamagazine.org':
            # Excluding possible repetitions
            if link['url'] in links:
                pass
            else:
                links.append(link['url'])

    print('page', page, 'cleared!')

    page+=1

with open('data/QMLinks', 'w') as out:
    for link in links:
        out.write(link)
        out.write('\n')

print('All done!')
