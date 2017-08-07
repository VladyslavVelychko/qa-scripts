from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--start-maximized")

driver = webdriver.Chrome(chrome_options=chrome_options)
heroku = driver.get('http://the-internet.herokuapp.com/')
form = driver.find_element_by_link_text('Form Authentication')
form.click()
driver.find_element_by_xpath('//*[@id="username"]').send_keys('tomsmith')
driver.find_element_by_xpath('//*[@id="password"]').send_keys('SuperSecretPassword!')
driver.find_element_by_xpath('//*[@type="submit"]').click()
#driver.quit()
