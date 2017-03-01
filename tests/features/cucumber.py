import datetime
import os
import time
import unittest

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from sys import platform
from lettuce import *
from nose.tools import assert_equals

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

#   Check the os platform of running computer
if platform == 'win32':
    driver_name = 'chromedriver'
else:
    driver_name = 'chromedriver_mac'

DRIVER_DIR = os.path.join(BASE_DIR, "chrome_driver", driver_name)
WAIT_TIME = 3  # wait time for browser to stay open for 3 seconds

base_url = 'http://www.ebay.ca/itm/161728962861'
driver = webdriver.Chrome(DRIVER_DIR)


@step(u'I am at ebay product page for the Oster blender "([^"]*)"')
def get_product_page(step, url):
    print('Go to Oster blender page...')
    driver.get(url)
    time.sleep(WAIT_TIME)


@step(u'I input a quantity of "([^"]*)" and add to shopping cart')
def add_quantity(step, quant):
    search_box = driver.find_element_by_id('qtyTextBox')
    search_box.send_keys(quant)
    driver.find_element_by_id('isCartBtn_btn').click()

@step(u'It will redirect to "([^"]*)" page')
def redirect_to_cart(step, expected_result):
    actual_result = driver.find_element_by_xpath('//*[@id="PageTitle"]/h1').text
    assert_equals(expected_result, actual_result)

@step(u'The "([^"]*)" is in the cart')
def verify_product(step, expected_result):
    actual_result = driver.find_element_by_xpath('//*[@id="161728962861_title"]/a').text
    assert_equals(expected_result, actual_result)

@step(u'Its quantity equal to "([^"]*)"')
def verify_quantify(step, expected_result):
    actual_result = driver.find_element_by_xpath('//*[@id="161728962861_title"]/parent::*/parent::*/parent::*/parent::*/div[2]/div[1]/div/input').value
    print actual_result
    assert_equals(expected_result, actual_result)
    driver.quit()
