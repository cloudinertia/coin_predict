from selenium import webdriver
import pickle


search_word = "apple"
MAXIMUM = 3
try:
    db = pickle.load(open('{}.json'.format(search_word),'rb'))
except:
    db = {} 

driver = webdriver.Chrome()

driver.get("https://www.google.co.kr/search?q={}".format(search_word))
driver.find_element_by_css_selector("a.q.qs").click()

def parse_content():
    articles = driver.find_elements_by_css_selector("div.g")
    for item in articles:
        
        title = item.find_element_by_css_selector('a.l._PMs').get_attribute('innerText')
        media = item.find_element_by_css_selector("div.slp > span._OHs").get_attribute('innerText')
        time = item.find_element_by_css_selector("div.slp > span.nsa").get_attribute('innerText')
        content = item.find_element_by_css_selector("div.st").get_attribute('innerText')

        db[title] = dict(
                media=media,
                time=time,
                content=content)

for i in range(MAXIMUM):
    parse_content()
    driver.execute_script
    next_button = driver.find_element_by_css_selector('#pnnext > span:nth-child(2)')
    driver.execute_script("arguments[0].scrollIntoView()",next_button)
    next_button.click()
    pickle.dump(db,open('{}.json'.format(search_word),'wb'))
