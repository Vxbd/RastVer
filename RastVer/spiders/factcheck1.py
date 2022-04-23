import scrapy

from bs4 import BeautifulSoup

class ToScrapeSpiderXPath(scrapy.Spider):
    name = "factcheck1"

    start_urls = [
        'https://mediabiasfactcheck.com/2022/03/18/the-latest-fact-checks-curated-by-media-bias-fact-check-03-18-2022/',
        'https://mediabiasfactcheck.com/2022/04/13/the-latest-fact-checks-curated-by-media-bias-fact-check-04-13-2022/',
        'https://mediabiasfactcheck.com/2022/04/12/the-latest-fact-checks-curated-by-media-bias-fact-check-04-12-2022/'
    ]


    def parse(self, response):
        # elem = response.css('table').css('tbody').css('tr')[0].css('td')[0].css('span').css('strong::text').getall()
        # elem = response.css('table').css('tbody').css('tr')[0].css('td').getall()

        # print("\n\n\n" )

        # soup = BeautifulSoup(elem)

        # print("\n\n\n" + soup.get_text() + "\n\n\n")

        table = response.xpath('//tbody')

        rows = table.xpath('//tr')

        row = rows[4]

        # col1 = row.xpath('td//text()')[0].extract()

        print("\n\n\n")
        # print(col1)
        print("\n\n\n")
        # col2 = row.xpath('td//text()')[1]
        # soup = BeautifulSoup(col2)

        print("\n\n\n")
        # print(soup.getText())
        print("\n\n\n")

        # row = rows[4]
        for row in rows:
            # cols = row.xpath('//td').getall()
            col = row.xpath('td//text()').extract()

            # print("\n\n\n")
            print(col)
            # print("\n\n\n")

            # Non usamos a sencia match (eq swtich) para permitir a compatibilidade con versions previas de python
            # Casos posibles
            """
            if col[1][0] == '\n':
                print("Etiqueta -> " + col[0] + col[1])
                print("Frase -> " + col[3])
            elif col[1][0] == '(':
                print("Etiqueta -> " + col[0])
                print("Frase -> " + col[4])
            else:
                print("Etiqueta -> " + col[0])
                print("Frase -> " + col[2])
            """

            # print("\n\n\n")
            # print("\n\n\n")
            filename = f'factcheck.txt'
            with open(filename, 'a') as f:
                f.write(str(col) + "\n")



