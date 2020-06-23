import requests 
from lxml import html 

for valores in weboot:
    weboot = requests.get('https://www.dafiti.com.br/roupas-masculinas/polos/'+str(valores)) 
    tree = html.fromstring(weboot.content)
    
    data = tree.xpath('//*[@id="wrapper"]/div[4]/div[2]/div[4]/div/div[2]"]')[0].value 
    print (str(data))