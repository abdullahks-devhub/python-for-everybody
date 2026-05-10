# import urllib.request, urllib.error
# from bs4 import BeautifulSoup
# import ssl

# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE

# url = input('Enter: ')
# html = urllib.request.urlopen(url, context=ctx).read()
# soup = BeautifulSoup(html, 'html.parser')

# count = input("Enter Count: ")
# count = int(count)
# pos = input("Enter Position: ")
# pos = int(pos)
# cou = 0
# cou2 = 0

# # Retrieve all of the span tags
# tags = soup('a')
# for tag in tags:
#     cou = cou+1
#     if(cou==pos):
#         print('Contents:', tag.contents[0])
#         cou2 += cou2
#     if(cou2==count):
#         break


import urllib.request, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Inputs
url = input('Enter URL: ').strip()
count = int(input("Enter count: "))
position = int(input("Enter position: "))

# Repeat process 'count' times
for i in range(count):
    print("Retrieving:", url)
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    
    # Find all anchor tags
    tags = soup('a')
    
    # Select the link at the given position (1-based index)
    tag = tags[position - 1]
    url = tag.get('href', None)   # Update URL for next loop
    name = tag.contents[0]

print("The answer to the assignment for this execution is", '"' + name + '"')
