import urllib.error, urllib.request, urllib.parse
import json
# import twurl

TWITTER_URL = 'http://api.twitter.com/1.1/friends/list.json'

while True:
    print('')
    acct = input('Input Twitter Acct: ')
    if len(acct) < 1:
        break
    url = twurl.augment(TWITTER_URL,
                        {'screen_name': acct, 'count': '5'})
    print('Retrieving', url)
    connection = urllib.request.urlopen(url)
    data = connection.read().decode()
    headers = dict(connection.getheaders())
    print('Remaining', headers['x-rate-limit-remaining'])
    js = json.loads(data)
    print(json.dumps(js, indent=4))

    for u in js['users']:
        print(u['screen_name'])
        s = u['status']['text']
        print('  ', s[:50])


