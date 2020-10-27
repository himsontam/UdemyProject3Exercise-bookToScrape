# UdemyProject3Exercise-bookToScrape
This is a Udemy tutorial to learn Scrapy. Modern Web Scraping with Python using Scrapy Splash Selenium

Link to scrapy: http://books.toscrape.com/

# Scrapy command:
- run scrapy script -----> scrapy crawl books

- run scrapy shell ------> scrapy shell

- Create New Scrpay Project -------> scrapy startproject bookToScrape

- You can start your first spider with:
  - cd imbd
  - scrapy genspider example example.com

- Create Scrapy spider -------> scrapy genspider books books.toscrape.com

- Create Scrapy spider with template -------> scrapy genspider -t crawl books books.toscrape.com

- scrapy genspider -l
  - Available templates: basic crawl csvfeed xmlfeed

- Export Excel Command -----> scrapy crawl books -o books_dataset.csv

- Export JSON Command ------> scrapy crawl books -o books_dataset.json

# Anaconda command:
- install dependencies ----> conda install -c conda-forge scrapy==1.6 pylint autopep8 -y
- install iPython ---------> conda install iPython
