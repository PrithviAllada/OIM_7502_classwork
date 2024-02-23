import scrapy
from scrapy.crawler import CrawlerProcess

class SP500YTDReturnSpider(scrapy.Spider):
    name = 'sp500_ytd_return'
    allowed_domains = ['slickcharts.com']
    start_urls = ['https://www.slickcharts.com/sp500/performance']

    def parse(self, response):
        # Loop over each table row in the tbody element
        for row in response.css('table.table > tbody > tr'):
            yield {
                'number': row.css('td:first-child::text').get(),
                'company': row.css('td:nth-child(2) a::text').get(),
                'symbol': row.css('td:nth-child(3) a::text').get(),
                # Extracting the text and excluding the image and spaces
                'ytd_return': row.css('td:nth-child(4)::text').re_first(r'\s*([\d.+-]+%)')
            }

# The file where the output will be saved
filename = "sp500_ytd_returns.csv"

# Create a CrawlerProcess with the spider and desired output format
process = CrawlerProcess(settings={
    'FEED_FORMAT': 'csv',
    'FEED_URI': filename
})

# Start the crawling process
process.crawl(SP500YTDReturnSpider)
process.start()
