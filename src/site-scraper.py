import requests
from bs4 import BeautifulSoup
import pickle
import datetime
from google_news_url_crawler import GoogleNewsURLCrawler

class SiteScraper:
    #인자1: url 리스트, 인자2: 얻어진 term 리스트를 파일로도 저장할 지 여부
    def scrap(self, urlsToScrap, writeToFile = bool):
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

        if(writeToFile == bool):
            pickle.dump(terms, open(str(datetime.datetime.now()) + '.terms', 'wb'))

        return terms

# 사용예시
# terms = siteScraper.scrap(googleNewsURLCrawler.next())
# print(terms)
# terms = siteScraper.scrap(googleNewsURLCrawler.next())
# print(terms)



