import requests
from bs4 import BeautifulSoup
import pickle
# import datetime
# from google_news_url_crawler import GoogleNewsURLCrawler

class SiteScraper:
    #인자1: url 리스트, 인자2: 얻어진 term 리스트를 저장할 파일 경로, 디폴트 값은 파일을 저장하지 않음
    def scrap(self, urlsToScrap, filePathToWrite=''):
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

        if filePathToWrite != '':
            pickle.dump(terms, open(filePathToWrite, 'wb'))

        return terms

# 사용예시
# googleNewsURLCrawler = GoogleNewsURLCrawler('stock market', 10)
# siteScraper = SiteScraper()
# terms = siteScraper.scrap(googleNewsURLCrawler.next(), str(datetime.datetime.now()) + '.terms')
# print(terms)
# terms = siteScraper.scrap(googleNewsURLCrawler.next())
# print(terms)



