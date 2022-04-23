import scrapy

class ToScrapeCSSSpider(scrapy.Spider):
    name = "factcheck"
    start_urls = [
        'https://mediabiasfactcheck.com/2022/03/18/the-latest-fact-checks-curated-by-media-bias-fact-check-03-18-2022/'
    ]

    def parse(self, response):


        elem = response.css('tbody').css('tr')[0]
        for aux in elem.css('td'):
            print("\n\n\n" + "\n\n\n")
            for i in aux.getall():
                print(str(i))

        filename = f'factcheck.txt'
        with open(filename, 'a') as f:
                f.write(response.text)


