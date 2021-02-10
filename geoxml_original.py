import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
#import ssl

#api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

# Ignore SSL certificate errors
#ctx = ssl.create_default_context()
#ctx.check_hostname = False
#ctx.verify_mode = ssl.CERT_NONE


url = input('Enter url: ')
print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved', len(data), 'characters')
    #print(data.decode())
tree = ET.fromstring(data) #parses XML from a string directly
    #into an Element, which is the root element of the parsed tree.

    #('comments/comment/count'))

counts = tree.findall('.//count')
counter = 0
summ = 0
for e in counts:
    counter += 1
    summ = summ + int(e.text)
print("Count: ", counter)
print("Sum: ", summ)

