from selenium import webdriver
import time


driver = webdriver.Chrome()

driver.maximize_window()

driver.get('https://www.python.org/')
time.sleep(2)

#digitar no campo de busca
driver.find_element_by_xpath('//*[@id="id-search-field"]').send_keys('python')

#clica no botão GO
driver.find_element_by_css_selector('#submit').click()

#imprimir texto

btn_txt = driver.find_element_by_id('submit').text

print(btn_txt)


