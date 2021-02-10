import urllib.request, urllib.parse, urllib.error
import json



url = input("Enter location: ")
print("Retrieving: ", url)
uh = urllib.request.urlopen(url) #connection
data = uh.read().decode()
print('Retrieved', len(data), 'characters')
#print(data)

info = json.loads(data) #the result is Python dictionary

count = 0
items = 0
for item in info['comments']:
    count = count + int(item['count'])
    items += 1
print('Count: ', items)
print('Sum: ', count)


