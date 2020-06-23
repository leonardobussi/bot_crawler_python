import requests
from lxml import html 
r = requests.get('https://dolarhoje.com/')
tree = html.fromstring(r.content)
data = tree.xpath('//*[@id="nacional"]')[0].value 

print(str(data))