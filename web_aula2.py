while True:
    import csv
    import requests 
    from lxml import html
    import os
    
    requisiçao = requests.get('https://www.terra.com.br/esportes/futebol/internacional/inglaterra/campeonato-ingles/tabela/')

    tree = html.fromstring(requisiçao.content)

    contador = 1
    linha = 1 

    while linha < 21:

        times = tree.xpath('//*[@id="mod-603-standings-round-robin"]/div[1]/div[1]/table/tbody/tr[%d]/td[3]/text ()' %contador)
        pontos = tree.xpath('//*[@id="mod-603-standings-round-robin"]/div[1]/div[1]/table/tbody/tr[%d]/td[5]/text ()' %contador)
        jogos = tree.xpath('//*[@id="mod-603-standings-round-robin"]/div[1]/div[1]/table/tbody/tr[%d]/td[6]/text()' %contador)
        vitorias = tree.xpath('/html/body/div[3]/div[2]/div[1]/div/div/div[1]/div[1]/table/tbody/tr[%d]/td[7]/text ()' %contador)
        empates = tree.xpath('/html/body/div[3]/div[2]/div[1]/div/div/div[1]/div[1]/table/tbody/tr[%d]/td[8]/text ()' %contador)
        derrotas = tree.xpath('/html/body/div[3]/div[2]/div[1]/div/div/div[1]/div[1]/table/tbody/tr[%d]/td[9]/text ()' %contador)
        golpro = tree.xpath('/html/body/div[3]/div[2]/div[1]/div/div/div[1]/div[1]/table/tbody/tr[%d]/td[10]/text ()' %contador)
        golcontra = tree.xpath('/html/body/div[3]/div[2]/div[1]/div/div/div[1]/div[1]/table/tbody/tr[%d]/td[11]/text ()' %contador)
        saldodegols = tree.xpath('/html/body/div[3]/div[2]/div[1]/div/div/div[1]/div[1]/table/tbody/tr[%d]/td[12]/text ()' %contador)
        aproveitamento = tree.xpath('/html/body/div[3]/div[2]/div[1]/div/div/div[1]/div[1]/table/tbody/tr[%d]/td[13]/text ()' %contador)
        
   
        txt = (str(times)+'|pontos'+str(pontos)+'|jogos '+str(jogos)+'|vitorias '+str(vitorias)+'|empates '+str(empates)+ '|derrotas '+str(derrotas)+'|gol pro '+str(golpro)+'|gol contra '+str(golcontra)+'|saldo de gols '+str(saldodegols)+'|aproveitamento '+str(aproveitamento) +'\n')

        linha = linha + 1
        contador = contador + 1  
        print(txt.replace(chr(93),'').replace(chr(91),'').replace(chr(39),'')) 
        ola = [times, pontos, jogos, vitorias, empates, derrotas, golpro, golcontra, saldodegols, aproveitamento]
        
        with open('tab_camp_ingles.csv','a') as oie:
            writer = csv.writer(oie)
            writer.writerow(ola)

    print ('.:: FIM DO BOOT ::.')

    opçao = input('Deseja repetir o processo? [s/n]')
    if opçao == 'n':
        break