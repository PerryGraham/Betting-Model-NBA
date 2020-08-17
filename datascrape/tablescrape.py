import scrapy 

class tableSpider(scrapy.Spider):
    name= 'table'
    
    start_urls =[
        "https://sportsdatabase.com/nba/query?output=default&sdql=date%2C+team%2C+site%2C+o%3Ateam%2C+total%2C++points%2C+o%3Apoints+%40season%3E2010&submit=++S+D+Q+L+%21++"
    ]

    def parse(self, response):
        table = response.xpath('//table[@id="outer"]//table//tr')
        #print(table.extract_first())
        for row in table[1:-53]: 
            yield {
               'date' : row.xpath('td[1]//text()').extract_first().replace('\n',""),
               'team' : row.xpath('td[2]//text()').extract_first().replace('\n',""),
                'site' : row.xpath('td[3]//text()').extract_first().replace('\n',""),
                'o:team' : row.xpath('td[4]//text()').extract_first().replace('\n',""),
                'total' : row.xpath('td[5]//text()').extract_first().replace('\n',""),
                'points' : row.xpath('td[6]//text()').extract_first().replace('\n',""),
                'o:points' : row.xpath('td[7]//text()').extract_first().replace('\n',"")
            }
        