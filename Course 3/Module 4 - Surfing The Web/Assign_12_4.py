import urllib.request, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter: ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the span tags
tags = soup('span')
total = 0
count = 0
for tag in tags:
    try:
        conv = int(tag.contents[0])  # Convert text inside span to int
        total += conv
        count += 1
    except:
        continue  # Skip if conversion fails (e.g., span has text instead of a number)

    print('TAG:', tag)
    print('Contents:', tag.contents[0])
    print('Attrs:', tag.attrs)

print('Count:', count)
print('Sum:', total)
