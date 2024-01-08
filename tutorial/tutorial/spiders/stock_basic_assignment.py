import scrapy
from pathlib import Path
import pandas as pd

class StockSpider(scrapy.Spider):
    name = "basic"
    start_urls = [
        "https://www.moneycontrol.com/stocks/marketstats/nsemact1/index.php?index=FNO"
    ]

    def parse(self, response):
            
            yield {
                "company_names": response.xpath("//*[@id='mc_content']/section/section/div[1]/div[2]/div/div/div[2]/table/tbody/tr/td[1]/h3/a/text()").getall(),
                "highs": response.xpath("//*[@id='mc_content']/section/section/div[1]/div[2]/div/div/div[2]/table/tbody/tr/td[2]/text()").getall(),
                "lows": response.xpath("//*[@id='mc_content']/section/section/div[1]/div[2]/div/div/div[2]/table/tbody/tr/td[3]/text()").getall(),
            }
            

def run_spider():
    from scrapy.crawler import CrawlerProcess
    from scrapy.utils.project import get_project_settings

    process = CrawlerProcess(get_project_settings())
    process.crawl(StockSpider)
    process.start()
    import pandas as pd
    stocks = pd.read_json('stocks.jsonl')
    print(stocks)

# If you want to run the spider directly when the script is executed
if __name__ == "__main__":
    run_spider()
