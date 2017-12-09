import requests
from bs4 import BeautifulSoup
#from google_news_url_crawler import GoogleNewsURLCrawler

class SiteScraper:
    #인자: url 리스트
    def scrap(self, urlsToScrap):
        terms = []

        for urlToScrap in urlsToScrap:
            try:
                get = requests.get(urlToScrap)
                beautifulSoap = BeautifulSoup(get.text)
                body = beautifulSoap.find('body')

            except Exception as message:
                print(message)
                continue;

            for tag in body.find_all():
                if((tag.name != 'script') and (tag.name != 'style')):
                    if(tag.string != None):
                        import re
                        try:
                            terms += list(filter(lambda element: (element != None) and (element != ''), re.split(r'\s+|\t+|\n+|,|:|;', tag.string)))

                        except Exception as message:
                            print(message)
                            continue;

        return terms

# 사용예시
# googleNewsURLCrawler = GoogleNewsURLCrawler('stock market', 10)
# siteScraper = SiteScraper()
# terms = siteScraper.scrap(googleNewsURLCrawler.next())
# print(len(terms))
# print(terms)
# terms = siteScraper.scrap(googleNewsURLCrawler.next())
# print(len(terms))
# print(terms)
# terms = siteScraper.scrap(googleNewsURLCrawler.next())
# print(len(terms))
# print(terms)


