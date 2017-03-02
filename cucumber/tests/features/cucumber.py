import os 															#used to find file paths

from nose.tools import assert_equals								#tool used with lettuce to check if the the actual result matches the expected result
from lettuce import *												#used to carry out testing with cucumber 
from selenium import webdriver										
from sys import platform											#used for determining the OS of the system

BASE_DIR = os.path.dirname(os.path.abspath(__file__))				#The directory of this file

#   Check the os platform of running computer
if platform == 'win32':												
    driver_name = 'chromedriver'									#windows driver if OS is windows
else:
    driver_name = 'chromedriver_mac'								#else try Mac driver

DRIVER_DIR = os.path.join(BASE_DIR, "chrome_driver", driver_name)	#full path to chromem river

base_url = 'http://www.ebay.ca/itm/161728962861'
driver = webdriver.Chrome(DRIVER_DIR)								#webdriver object


# 1. Normal Flow
@step(u'I am at the ebay product page for the Oster blender "([^"]*)"')			
def get_product_page(step, url):
    driver.get(url)															#go to the url specified in step definition


@step(u'I input a quantity of "([^"]*)" and add to shopping cart')
def add_positive_quantity(step, quant):
    search_box = driver.find_element_by_id('qtyTextBox')					#find the quantity textbox on page by ID
    search_box.clear()														#clear default value
    search_box.send_keys(quant)												#enter the quantity specified by step definition
    driver.find_element_by_id('isCartBtn_btn').click()						#click submit button


@step(u'It will redirect to "([^"]*)" page')
def redirect_to_cart(step, expected_result):
    actual_result = driver.find_element_by_xpath('//*[@id="PageTitle"]/h1').text 			#get the page title
    assert_equals(expected_result, actual_result)											#check that the page title matches


@step(u'The "([^"]*)" is in the cart')
def verify_product(step, expected_result):
    actual_result = driver.find_element_by_xpath('//*[@id="161728962861_title"]/a').text 	#find the blender on cart page by its product id
    assert_equals(expected_result, actual_result)											#check expected name matches result


@step(u'Its quantity is equal to "([^"]*)"')
def verify_quantify(step, expected_result):
    actual_result = driver.find_element_by_xpath(
        '//*[@id="161728962861_title"]/parent::*/parent::*/parent::*/parent::*/div[2]/div[1]/div/input').get_attribute(
        'value')																			#get the value of the quantity box of the blender by relative path from its name specified by ID
    assert_equals(expected_result, actual_result)											#check correct quantity as defined by step definition is in the cart


# 2. Alternative Flow
@step(u'I am at the shopping cart page "([^"]*)"')
def get_to_cart_page(step, url):
    driver.get(url)																			#go to shopping cart page


@step(u'I edit the quantity to "([^"]*)" and click update')
def edit_quantity(step, quant):
    quantity_box = driver.find_element_by_xpath(
        '//*[@id="161728962861_title"]/parent::*/parent::*/parent::*/parent::*/div[2]/div[1]/div/input')
    																						#Go to quantity textbox via relative path
    quantity_box.clear()																	#clear quantity box
    quantity_box.send_keys(quant)															#enter new quantity
    driver.find_element_by_xpath(
        '//*[@id="161728962861_title"]/parent::*/parent::*/parent::*/parent::*/div[2]/div[1]/div/div/a').click()
    																						#find update link by relative path and click

@step(u'It will reload the page and show the new quantity "([^"]*)"')
def two_verify_quantify(step, expected_result):
    actual_result = driver.find_element_by_xpath(
        '//*[@id="161728962861_title"]/parent::*/parent::*/parent::*/parent::*/div[2]/div[1]/div/input').get_attribute(
        'value')																			#check quantity box value
    assert_equals(expected_result, actual_result)											#check result matches step definition expected value


# 3. Error Flow
@step(u'I am on the ebay product page for the Oster blender "([^"]*)"')
def c_get_product_page(step, url):
    driver.get(url)																			#go to blender product page


@step(u'I input an invalid quantity of "([^"]*)"')
def c_add_negative_quantity(step, quant):
    quantity_box = driver.find_element_by_id('qtyTextBox')									#find quantity box by ID
    quantity_box.clear()																	#clear textbox
    quantity_box.send_keys(quant)															#enter quantity in step definition


@step(u'It should indicate error "([^"]*)"')
def display_error(step, expected_error):
    actual_error = driver.find_element_by_id('w1-13-_errMsg').text 							#look for the expected error message by ID
    assert_equals(expected_error, actual_error)												#check error message exists and is the expected message given by step definition
    driver.quit()																			#last test quit driver
