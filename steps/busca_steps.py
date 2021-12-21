from behave import given, when, then
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()


@given(u'que acesso o site do python')
def step_impl(context):
    driver.get("https://www.python.org/")


@given(u'preencho o input de pesquisa')
def step_impl(context):
    driver.find_element_by_xpath('//*[@id="id-search-field"]').send_keys('python')


@when(u'clico no botão de pesquisar')
def step_impl(context):
    driver.find_element_by_css_selector('#submit').click()



@then(u'devo visualizar os resultados da pesquisa')
def step_impl(context):
    driver.find_element_by_css_selector('#submit').click()
    btn_txt = driver.find_element_by_id('submit').text
    print(btn_txt)