from selenium import webdriver
import os
import datetime
from corpus import Corpus

class GoogleNewsURLCrawler:
    chromeDriver = None

    #인자1: 검색 키워드, 인자2: 한번의 검색 쿼리로 리턴할 결과들의 수
    def __init__(self, keyword = '', pageSizeToRetreive = 10):
        GoogleNewsURLCrawler.__InitializeChromeDriver()
        self.__initialize(keyword, pageSizeToRetreive)

    def __initialize(self, keyword, pageSizeToRetreive):
        self.pageCount = 0
        self.pageSizeToRetreive = pageSizeToRetreive
        self.keyword = keyword
        self.queryExpression = GoogleNewsURLCrawler._GetFormattedQueryExpressionForGoogleSearch(keyword)

    #내부 유틸(private)
    @classmethod
    def __InitializeChromeDriver(cls):
        if (cls.chromeDriver == None):
            cwd = os.getcwd()
            cls.chromeDriver = webdriver.Chrome(cwd + '/chromedriver')
            cls.chromeDriver.implicitly_wait(10)

    # 내부 유틸(private)
    @classmethod
    def _GetFormattedQueryExpressionForGoogleSearch(cls, keyword):
        queryExpression = ''

        splittedKeywords = keyword.split()
        if(1 <= len(splittedKeywords)):
            queryExpression += splittedKeywords[0]
            del splittedKeywords[0]

            for splittedKeyword in splittedKeywords:
                queryExpression += ('+' + splittedKeyword)

        return queryExpression

    # 내부 유틸(private)
    @classmethod
    def _getNextSearchURL(cls, queryExpression, pageCount, pageSizeToRetreive):
        return 'https://www.google.com/search?q={}&start={}&tbm=nws&num={}&hl=en'.format(queryExpression, pageCount, pageSizeToRetreive)

    @classmethod
    def _GetToday(cls):
        return "{:%b %d, %Y}".format(datetime.datetime.today())

    #다음 크롤링 결과를 얻어옴
    def next(self):
        urls = []

        searchURL = GoogleNewsURLCrawler._getNextSearchURL(self.queryExpression, self.pageCount, self.pageSizeToRetreive)
        self.pageCount += self.pageSizeToRetreive

        GoogleNewsURLCrawler.chromeDriver.get(searchURL)
        searchResults = GoogleNewsURLCrawler.chromeDriver.find_elements_by_class_name('_hJs')

        for searchResult in searchResults:
            try:
               link = searchResult.find_element_by_tag_name('h3').find_element_by_tag_name('a').get_attribute('href')
               date = searchResult.find_element_by_class_name('slp').find_element_by_class_name('_QHs').get_attribute('innerText')
               if date.find('ago') != -1:
                   date = GoogleNewsURLCrawler._GetToday()

               urls.append((link, date))
            except Exception as errorMessage:
                print(errorMessage)
                continue

        corpora = []
        for url in urls:
            try:
                GoogleNewsURLCrawler.chromeDriver.get(url[0])
                terms = ''

                try:
                    for element in GoogleNewsURLCrawler.chromeDriver.find_element_by_tag_name('body').find_elements_by_xpath(".//*"):
                        if (element.tag_name != 'style') and (element.tag_name != 'script'):
                            import re
                            try:
                                innerText = element.get_attribute('innerText')
                                if innerText != None:
                                    tokens = list(filter(lambda element: (element != None) and (element != ''),
                                                         re.split(r'\s+|\t+|\n+|,|:|;|\.', innerText)))
                                    for token in tokens:
                                        terms += (token + ' ')

                            except Exception as ex:
                                print('exception: ' + ex + 'exception text: ' + innerText)
                                print('\n')
                                print('\n')
                                continue

                except Exception:
                    continue

                corpora.append(Corpus(self.keyword, url[1], url[0], terms))
            except Exception:
                continue

        return corpora

    #크롤링 조건을 리셋하여 다시 검색
    #인자1: 검색 키워드, 인자2: 한번의 검색 쿼리로 리턴할 결과들의 수
    def reset(self, keyword, pageSizeToRetreive):
        self.__initialize(keyword, pageSizeToRetreive)


#예제
# def updateDataBase(keyword, page):
#     googleNewsURLCrawler = GoogleNewsURLCrawler(keyword, page)
#
#     resultPage = googleNewsURLCrawler.next()
#     for result in resultPage:
#         result.save()
#
# updateDataBase('MSFT', 10)


