import schedule
import time
from tutorial.spiders.stock_basic_assignment import run_spider

def job():
    print("Running the Scrapy spider...")
    run_spider()  # Call your Scrapy spider function here

# Schedule the job to run every hour
schedule.every(1).hour.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
