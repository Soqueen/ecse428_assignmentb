import os

from nose.tools import assert_equals
from lettuce import *
from selenium import webdriver
from sys import platform

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

#   Check the os platform of running computer
if platform == 'win32':
    driver_name = 'chromedriver'
else:
    driver_name = 'chromedriver_mac'

DRIVER_DIR = os.path.join(BASE_DIR, "chrome_driver", driver_name)

base_url = 'http://www.ebay.ca/itm/161728962861'
driver = webdriver.Chrome(DRIVER_DIR)


# 1. Normal Flow
@step(u'I am at the ebay product page for the Oster blender "([^"]*)"')
def get_product_page(url):
    driver.get(url)


@step(u'I input a quantity of "([^"]*)" and add to shopping cart')
def add_positive_quantity(quant):
    search_box = driver.find_element_by_id('qtyTextBox')
    search_box.clear()
    search_box.send_keys(quant)
    driver.find_element_by_id('isCartBtn_btn').click()


@step(u'It will redirect to "([^"]*)" page')
def redirect_to_cart(expected_result):
    actual_result = driver.find_element_by_xpath('//*[@id="PageTitle"]/h1').text
    assert_equals(expected_result, actual_result)


@step(u'The "([^"]*)" is in the cart')
def verify_product(expected_result):
    actual_result = driver.find_element_by_xpath('//*[@id="161728962861_title"]/a').text
    assert_equals(expected_result, actual_result)


@step(u'Its quantity is equal to "([^"]*)"')
def verify_quantify(expected_result):
    actual_result = driver.find_element_by_xpath(
        '//*[@id="161728962861_title"]/parent::*/parent::*/parent::*/parent::*/div[2]/div[1]/div/input').get_attribute(
        'value')
    assert_equals(expected_result, actual_result)


# 2. Alternative Flow
@step(u'I am at the shopping cart page "([^"]*)"')
def get_to_cart_page(url):
    driver.get(url)


@step(u'I edit the quantity to "([^"]*)" and click update')
def edit_quantity(quant):
    search_box = driver.find_element_by_xpath(
        '//*[@id="161728962861_title"]/parent::*/parent::*/parent::*/parent::*/div[2]/div[1]/div/input')
    search_box.clear()
    search_box.send_keys(quant)
    driver.find_element_by_xpath(
        '//*[@id="161728962861_title"]/parent::*/parent::*/parent::*/parent::*/div[2]/div[1]/div/div/a').click()


@step(u'It will reload the page and show the new quantity "([^"]*)"')
def two_verify_quantify(expected_result):
    actual_result = driver.find_element_by_xpath(
        '//*[@id="161728962861_title"]/parent::*/parent::*/parent::*/parent::*/div[2]/div[1]/div/input').get_attribute(
        'value')
    assert_equals(expected_result, actual_result)


# 3. Error Flow
@step(u'I am on the ebay product page for the Oster blender "([^"]*)"')
def c_get_product_page(url):
    driver.get(url)


@step(u'I input an invalid quantity of "([^"]*)"')
def c_add_negative_quantity(quant):
    search_box = driver.find_element_by_id('qtyTextBox')
    search_box.clear()
    search_box.send_keys(quant)


@step(u'It should indicate error "([^"]*)"')
def display_error(expected_error):
    actual_error = driver.find_element_by_id('w1-13-_errMsg').text
    assert_equals(expected_error, actual_error)
    driver.quit()
