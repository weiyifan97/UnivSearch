from os import listdir
from stringsParser import *
import concurrent.futures, json

pages = listdir('data/pages')

def search(name):
    """ count how many times 'name' has been mentioned"""
    count = 0
    for page in pages:
        with open('data/pages/'+page) as texts:
            for line in texts:
                count += line.count(name[:-1])
    return count

raw_result = {}

# multiprocessing
with open('data/Universities') as Univs:
    univs = Univs.readlines()
    t = 0
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for name, times in zip(univs, executor.map(search, univs)):
            t += 1
            raw_result[name] = times
            if t % 50 == 0:
                print('cleared', t)

# excluding duplications
# Explain: string 'a' is a part of 'ab', so the count of 'a' is bigger than
# the actual count of 'a' plus the count of 'ab'
def exclude(name):
    times = raw_result[name]
    for child in children(name, univs):
        times -= raw_result[child]

    return times

result = []
with concurrent.futures.ProcessPoolExecutor() as executor:
    for name, times in zip(univs, executor.map(exclude, univs)):
        result.append([times, name])

result.sort(reverse=True)
with open('result', 'w') as out:
    out.write(json.dumps(result))

print('Mentioned', '\t', 'Name')
for res in result[:15]:
    print(res[0], '\t', res[1])
