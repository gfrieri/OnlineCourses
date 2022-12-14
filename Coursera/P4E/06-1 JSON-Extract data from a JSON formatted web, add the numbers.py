import urllib.request, urllib.parse, urllib.error
import ssl
import json

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    url = input('Enter location: ')
    if len(url) < 1: break

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read()
    print('Retrieved', len(data), 'characters')
    info = json.loads(data)
    #print(info['comments'][0]['count'])

    sum = 0
    for item in info['comments']:
        count = int(item['count'])
        print('\nCount:', count)
        sum = sum + count
        print('Sum:', sum)