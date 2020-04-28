import json
from difflib import get_close_matches

data = json.load(open('data.json'))
dataKeys = data.keys()

def checkKey(keyword):
    loweredKeyword = keyword.lower()
    if loweredKeyword not in data:
        matches = get_close_matches(loweredKeyword, dataKeys, n=1, cutoff=0.8)
        print('Did you mean {}?'.format(','.join(matches)))
    else:
        print(data[loweredKeyword]) 

keyword = input('Enter your search key: ')

checkKey(keyword)