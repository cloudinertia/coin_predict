import requests
from bs4 import BeautifulSoup
from google_news_url_crawler import GoogleNewsURLCrawler

class SiteScraper:
    #인자: url리스트
    def scrap(self, urlsToScrap):
        terms = []
        for urlToScrap in urlsToScrap:
            get = requests.get(urlToScrap)
            beautifulSoap = BeautifulSoup(get.text)

            body = beautifulSoap.find('body')
            for tag in body.find_all():
                if((tag.name != 'script') and (tag.name != 'style')):
                    if(tag.string != None):
                        import re
                        terms += list(filter(lambda element: (element != None) and (element != ''), re.split(r'\s+|\t+|\n+|,|:|;', tag.string)))

        return terms

# 사용예시
# googleNewsURLCrawler = GoogleNewsURLCrawler('stock market', 20)
# siteScraper = SiteScraper()
# print(str(len(siteScraper.scrap(googleNewsURLCrawler.next()))))

