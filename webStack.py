import re
from threading import Thread
import requests

def get_links(url):
    req = get_req(url)
    if(req is not None):
        html = req.text
        urls = re.findall('(?<=href=["\'])https?://.+?(?=["\'])', html)
        return urls
    return None

def get_req(url):
    try:
        req = s.get(url)
        return req
    except Exception:
        print('[-] Erro ao ir buscar página: ', url)
        return None

def inject_links(data, url):
    urls = get_links(url)
    if(urls is not None):
        for url in urls:
            if(url not in data and len(data) < urls_max):
                data.add(url) # adicionamos aos urls crawled
                print('[+] Total: {} [+] putting: {} '.format(len(data), url))
                return inject_links(data, url)
    return

def producer(url, threadNum):
    while len(data) < urls_max:
        inject_links(data, url)
    #print('\n', data) # comentar isto depois de ter percebido, este print e muito pesado 
    print('[+] Terminated - killing thread {} -> Total urls stored: {}'.format(threadNum, len(data)))
    # aqui pode escrever para um ficheiro por exemplo

data = set()
urls_max = 100
threads = 10
start_urls = ['http://pt.stackoverflow.com/', 'http://www.w3schools.com/default.asp', 'http://spectrum.ieee.org/']

s = requests.Session()
for i in range(len(start_urls)):
    for j in range(threads):
        t = Thread(target=producer, args=(start_urls[i], '{}.{}'.format(i+1, j+1)))
        t.start()