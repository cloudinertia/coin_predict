from selenium import webdriver
import os

class GoogleNewsURLCrawler:
    chromeDriver = None

    def __init__(self, keyword, pageSizeToRetreive):
        GoogleNewsURLCrawler.InitializeChromeDriver()

        self.pageCount = 0
        self.pageSizeToRetreive = pageSizeToRetreive
        self.queryExpression = GoogleNewsURLCrawler.GetFormattedQueryExpressionForGoogleSearch(keyword)

    @classmethod
    def InitializeChromeDriver(cls):
        if (cls.chromeDriver == None):
            cwd = os.getcwd()
            cls.chromeDriver = webdriver.Chrome(cwd + '/chromedriver')
            cls.chromeDriver.implicitly_wait(10)

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

    def getNextSearchURL(self):
        return 'https://www.google.com/search?q={}&start={}&tpe=nws&num={}&hl=en&tpe=nws'.format(self.queryExpression, self
                                                                                                 .pageCount, self.pageSizeToRetreive)


    def next(self):
        searchURL = self.getNextSearchURL()
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