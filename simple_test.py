"""This script open a Firefox browser
    and try to access Python page"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

DRIVER = webdriver.Firefox()
DRIVER.get('http://www.python.org')
assert 'Python' in DRIVER.title
ELEM = DRIVER.find_element_by_name('q')
ELEM.clear()
ELEM.send_keys('pycon')
ELEM.send_keys(Keys.ENTER)
assert 'No results found.' not in DRIVER.page_source
DRIVER.close()
