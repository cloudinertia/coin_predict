import pickle
import os

class Corpus:
    def __init__(self, keyword, date, url, terms):
        self.keyword = keyword
        self.date = date
        self.url = url
        self.terms = terms

    def save(self):
        if self.saveURL() == True:
            self.saveTerms()


    def saveURL(self):
        filePath = os.getcwd() + '/' + self.keyword + '_' + self.date + '.urls'
        try:
            urlFile = open(filePath, 'rt')
            urlList = urlFile.read()
            urlFile.close()

            if self.url not in urlList:
                try:
                    urlFile = open(filePath, 'at')
                    urlFile.write(' ' + self.url)
                    urlFile.close()
                except IOError as error:
                    print("file error: " + error)
                    return False

                return True
            else:
                return False

        except IOError:
            try:
                urlFile = open(filePath, 'wt')
                urlFile.write(self.url)
                urlFile.close()
            except IOError as error:
                print("file error: " + error)
                return False

            return True

    def saveTerms(self):
        try:
            filePath = os.getcwd() + '/' + self.keyword + '_' + self.date + '.corpus'
            corpusFile = open(filePath, 'at')
            corpusFile.write(self.terms + ' ')
            corpusFile.close()

        except IOError as error:
            print("file error: " + error)

textNumber = 0
def generateText():
    global textNumber
    textNumber += 1
    return 'text' + str(textNumber)

urlNumber = 0
def generateURL():
    global  urlNumber
    urlNumber += 1
    return 'url' + str(urlNumber)


