from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests

chrome_options = Options()
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(chrome_options=chrome_options)


def urlparse(url):
    driver.get(url)
    if requests.get(url).status_code == 200:
        title = driver.title
        meta_desc = driver.find_element_by_xpath("//meta[@property='og:description']").get_attribute('content')
        h1 = driver.find_elements_by_tag_name('h1')
        return title, meta_desc, h1
    else:
        return 'Fail'


link1 = urlparse('http://github.com/')
link2 = urlparse('https://github.com/')
link3 = urlparse('https://www.github.com/')
link4 = urlparse('https://www.github.com/test/')
link5 = urlparse('https://github.com/testlololo')
link6 = urlparse('https://github.com/test?lol')
