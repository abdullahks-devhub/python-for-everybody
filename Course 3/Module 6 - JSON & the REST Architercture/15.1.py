import json
import urllib.request

url = input('Enter location: ')
print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read().decode()   # decode bytes to string
print('Retrieved', len(data), 'characters')

info = json.loads(data)

count = 0
sum = 0
for item in info['comments']:
    val = item['count']
    val = int(val)
    sum += val
    count += 1

print("Value:", sum)
print("Count:", count)
