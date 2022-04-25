import scrapy

#Biblioteca para procesado de texto
from bs4 import BeautifulSoup

#Obxectos que imos empregar
from RastVer.spiders import New


class ToScrapeSpiderXPath(scrapy.Spider):
    name = "factcheck2"

    posiblesRate = ["FALSE", "BLATANT-LIE", "MOSTLY-TRUE", "MOSTLY-FALSE", "NO-EVIDENCE", "TRUE"]

    visitadas = []

    novas = dict()

    start_urls = [
        "https://mediabiasfactcheck.com/category/fact-check-2/"
#        'https://mediabiasfactcheck.com/2022/03/18/the-latest-fact-checks-curated-by-media-bias-fact-check-03-18-2022/'
    ]


    def parse(self, response):


        print("\n\n\n")
        print(response.url)
        url_parts = response.url.split(sep='/')
        print("\n\n\n")
        print(url_parts[3])


        #En funcioón da url distinguimos se é de enlaces ou de información
        if (url_parts[3] == 'category'):
            print("-------------------- PAXINA DE ENLACES --------------------")

            #Creamos unha lista onde iremos almacenando os enlaces dos artigos
            enlaces = []

            #Obtemos unha lista de articles da páxina
            articles = response.xpath('.//article')
            #print("O número de artigos é :" + str(len(articles)))

            #Para cada artigo tratamos de extraer o seu enlace
            for article in articles:

                #Obtemos o titulo H3 que conten o enlace
                h3 = article.xpath('.//h3')

                #Verificamos que exista só un elemento
                if len(h3) != 1:
                    print("Existe un erro na verificación no número de titulos esperados H3  -- " + str(len(h3)))


                #Buscamos os enlaces e estremolos
                enlace = h3[0].xpath('.//a/@href').extract()

                # Verificamos que exista só un elemento
                if len(enlace) != 1:
                    print("Existe un erro na verificación no número de enlaces esparados  -- " + str(len(enlaces)))

                #Imprimimos e gardamos o enlace
                #print("O artigo é " + str(articles.index(article)) + " enlace:   " + enlace[0])

                enlaces.append(enlace[0])

            #print("\n\n\n" + "\n".join(enlaces) +"\n\n\n")

            #Buscamos o elemento que ten o indice
            div = response.xpath('//div[@class="pagination clearfix"]')

            #Obtemos os enlaces das seguintes páxinas
            seguintes = div.xpath('.//a/@href').extract()

            #print("Enlaces:" + "\n\n\n" + "\n".join(seguintes) +"\n\n\n")

            #Engadimos só o seguinte enlace a lista de enlaces
            for seguinte in seguintes:
                if seguinte not in self.visitadas:
                    enlaces.append(seguinte)

            for enlace in enlaces:
                self.visitadas.append(enlace)
                yield scrapy.Request(response.urljoin(enlace))

        else:
            print("-------------------- PAXINA DE INFORMACIÓN --------------------")

            filename = f'factcheck.txt'
           # with open(filename, 'a') as f:
            #    f.write(response.url + "\n")

            #Selecionamos a tabla
            table = response.xpath('//tbody')
            #Seleccionamos a fila
            rows = table.xpath('.//tr')

            #print(str(rows))

            #Extremos o contido
            for row in rows:
                col = row.xpath('td//text()').extract()
                #print("\n\n\n")
                #print(col)

                #Creamos a nova
                nova = New.New()

                #Collemos o rate ditinguindo se é de unha ou duas liñas
                if '\n' in col[1]:
                    nova.rate = col[0] + col[1].replace("\n", "-")
                else:
                    nova.rate = col[0]

                #Comprobamos que sexa unha clasificación valida e senon reintentamos
                if not nova.rate in self.posiblesRate:
                    for element in col:
                        if 'ating:' in element:
                            pos = col.index(element)
                            nova.rate = col[pos+1]


                #Buscamos o claim
                #Mejoraría el rendimiento sin los breaks
                for element in col:
                    if 'laim' in element and ':' in element:
                        pos = col.index(element)
                        if col[pos + 1] == ' ' and len(col[pos + 1]) == 1:
                            nova.claim = col[pos + 2]
                        elif ':' in col[pos + 1]:
                            nova.claim = col[pos + 2]
                        else:
                            nova.claim = col[pos + 1]
                    elif '):' in element:
                        pos = col.index(element)
                        nova.claim = col[pos + 1]
                    elif ')' in element:
                        pos = col.index(element)
                        if ':' in col[pos + 1]:
                            nova.claim = col[pos + 2]

                #print("\n\n\n")

                #Gardamolo no ficheiro
                filename = f'factcheck.txt'
                with open(filename, 'a') as f:
                    f.write(nova.rate + '----' + nova.claim + "\n" + str(col) + '\n')
                    #f.write(str(col) + "\n")


        print("\n\n\n")
