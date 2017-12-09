from selenium import webdriver
import os

class GoogleNewsURLCrawler:
    chromeDriver = None

    #인자1: 검색 키워드, 인자2: 한번의 검색 쿼리로 리턴할 결과들의 수
    def __init__(self, keyword, pageSizeToRetreive):
        GoogleNewsURLCrawler.InitializeChromeDriver()

        self.pageCount = 0
        self.pageSizeToRetreive = pageSizeToRetreive
        self.queryExpression = GoogleNewsURLCrawler.GetFormattedQueryExpressionForGoogleSearch(keyword)

    #내부 유틸
    @classmethod
    def InitializeChromeDriver(cls):
        if (cls.chromeDriver == None):
            cwd = os.getcwd()
            cls.chromeDriver = webdriver.Chrome(cwd + '/chromedriver')
            cls.chromeDriver.implicitly_wait(10)

    # 내부 유틸
    @classmethod
    def GetFormattedQueryExpressionForGoogleSearch(cls, keyword):
        queryExpression = ''

        splittedKeywords = keyword.split()
        if(1 <= len(splittedKeywords)):
            queryExpression += splittedKeywords[0]
            del splittedKeywords[0]

            for splittedKeyword in splittedKeywords:
                queryExpression += ('+' + splittedKeyword)

        return queryExpression

    # 내부 유틸
    @classmethod
    def getNextSearchURL(cls, queryExpression, pageCount, pageSizeToRetreive):
        return 'https://www.google.com/search?q={}&start={}&tpe=nws&num={}&hl=en&tpe=nws'.format(queryExpression, pageCount, pageSizeToRetreive)


    def next(self):
        searchURL = GoogleNewsURLCrawler.getNextSearchURL(self.queryExpression, self.pageCount, self.pageSizeToRetreive)
        self.pageCount += self.pageSizeToRetreive

        self.chromeDriver.get(searchURL)
        searchResults = self.chromeDriver.find_elements_by_class_name('rc')

        urls = []
        for searchResult in searchResults:
            try:
                headLineOfSearchResult = searchResult.find_element_by_tag_name('h3')
                linkElement = headLineOfSearchResult.find_element_by_tag_name('a')
                urls.append(linkElement.get_attribute('href'))
                print(linkElement.get_attribute('href'))
            except Exception as errorMessage:
                print(errorMessage)
                continue



        return urls

# 사용법 예시
# googleNewsURLCrawler = GoogleNewsURLCrawler('stock market', 20)
# googleNewsURLCrawler.next()
# print('\n')
# googleNewsURLCrawler.next()
# print('\n')
# googleNewsURLCrawler.next()