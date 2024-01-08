# Stock Data Scraper

A web scraping tool built with Scrapy to extract stock market data from MoneyControl.

## Introduction

Stock Data Scraper is a Python web scraping tool that extracts stock market data, including company names, highs, and lows, from the MoneyControl website.

## Features

- Extracts company names, highs, and lows from the stock market page on MoneyControl.

## Getting Started

### Prerequisites

Make sure you have the following installed:

- Python (version 3.x)
- Scrapy
- Pandas
### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/stock-data-scraper.git
2. Run the cfollowing commands in terminal
  - If u want to directly run the script for web scraping, run this command in terminal after changing to the project-specific directory:
    scrapy crawl basic -o output.json
  - If u want it to run every hour:
     python recurring.py
