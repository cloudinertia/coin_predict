from selenium import webdriver
import os

class GoogleNewsURLCrawler:
    chromeDriver = None

    #인자1: 검색 키워드, 인자2: 한번의 검색 쿼리로 리턴할 결과들의 수
    def __init__(self, keyword, pageSizeToRetreive):
        GoogleNewsURLCrawler.__InitializeChromeDriver()
        self.__initialize(keyword, pageSizeToRetreive)

    def __initialize(self, keyword, pageSizeToRetreive):
        self.pageCount = 0
        self.pageSizeToRetreive = pageSizeToRetreive
        self.queryExpression = GoogleNewsURLCrawler.__GetFormattedQueryExpressionForGoogleSearch(keyword)

    #내부 유틸(private)
    @classmethod
    def __InitializeChromeDriver(cls):
        if (cls.chromeDriver == None):
            cwd = os.getcwd()
            cls.chromeDriver = webdriver.Chrome(cwd + '/chromedriver')
            cls.chromeDriver.implicitly_wait(10)

    # 내부 유틸(private)
    @classmethod
    def __GetFormattedQueryExpressionForGoogleSearch(cls, keyword):
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
    def __getNextSearchURL(cls, queryExpression, pageCount, pageSizeToRetreive):
        return 'https://www.google.com/search?q={}&start={}&tpe=nws&num={}&hl=en&tpe=nws'.format(queryExpression, pageCount, pageSizeToRetreive)


    #다음 크롤링 결과를 얻어옴
    def next(self):
        searchURL = GoogleNewsURLCrawler.__getNextSearchURL(self.queryExpression, self.pageCount, self.pageSizeToRetreive)
        self.pageCount += self.pageSizeToRetreive

        self.chromeDriver.get(searchURL)
        searchResults = self.chromeDriver.find_elements_by_class_name('rc')

        urls = []
        for searchResult in searchResults:
            try:
                headLineOfSearchResult = searchResult.find_element_by_tag_name('h3')
                linkElement = headLineOfSearchResult.find_element_by_tag_name('a')
                urls.append(linkElement.get_attribute('href'))
            except Exception as errorMessage:
                print(errorMessage)
                continue



        return urls

    #크롤링 조건을 리셋하여 다시 검색
    #인자1: 검색 키워드, 인자2: 한번의 검색 쿼리로 리턴할 결과들의 수
    def reset(self, keyword, pageSizeToRetreive):
        self.__initialize(keyword, pageSizeToRetreive)

# 사용법 예시
# googleNewsURLCrawler = GoogleNewsURLCrawler('stock market', 20)
# print(googleNewsURLCrawler.next())
# print('\n')
# print(googleNewsURLCrawler.next())
# print('\n')
# googleNewsURLCrawler.reset('bitcoin', 10)
# print(googleNewsURLCrawler.next())