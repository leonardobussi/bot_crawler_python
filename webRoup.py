import requests 
from lxml import html
r = requests.get('https://www.centauro.com.br/?origem=google_kenshoo&utm_source=google_brand&utm_medium=SCH_BRT_Centauro_Exata&utm_campaign=Centauro_Exata&utm_keyword=&matchtype=&gclid=EAIaIQobChMI-7GmwrnP3gIVEYWRCh2EIgCkEAAYASAAEgI8SfD_BwE')
t = html.fromstring(r.content)
print(str(t))
texto = t.xpath('/html/body/nav/div[1]/ul/li[3]/text()')[0].value
print (str(texto))