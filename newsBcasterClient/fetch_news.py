import requests

import scrapy


def crawl_news():
    lines = ""
    url = "http://www.aninews.in/rssfeed/10-general-news.html"
    page_src = requests.get(url)
    page_src = page_src.text
    news = scrapy.Selector(text=page_src).xpath('//title/text()').extract()
    for line in news:
        line = line.strip()
        lines = line + " | " + lines
    return lines