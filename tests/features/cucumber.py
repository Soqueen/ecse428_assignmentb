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
    actual_result = driver.find_element_by_xpath('//*[@id="qty_6984146269"]').text
    assert_equals(expected_result, actual_result)
    driver.quit()


# class ChromeTest(unittest.TestCase):
#     # Anything declared in setUp will be executed for all test cases
#     def setUp(self):
#         # clear database
#         self.driver = webdriver.Chrome(DRIVER_DIR)
#         self.base_url = 'http://www.ebay.ca/itm/161728962861'
#
#     def test_normal_flow(self):
#         driver = self.driver
#         driver.get(self.base_url)
#
#     def test_alternative_flow(self):
#         driver = self.driver
#         driver.get(self.base_url)
#
#     def test_error_flow(self):
#         driver = self.driver
#         driver.get(self.base_url)
#
#     def take_screen_shot(self, test_name):
#         """
#         Taking screen shot of the test result. The purpose is need when the test fail
#         :param test_name: Name of screen shot
#         :return:
#         """
#         now = datetime.datetime.now()
#         directory = os.path.join(BASE_DIR, 'test_results_img', now.strftime("%Y-%m-%d"))
#         if not os.path.exists(directory):
#             os.makedirs(directory)
#         image_name = '.'.join([test_name + now.strftime("_%H:%M:%S"), 'png'])
#         return self.driver.save_screenshot(os.path.join(directory, image_name))
#
#     # Anything declared in tearDown will be executed for all test cases
#     def tearDown(self):
#         # Close the browser.
#         self.driver.quit()

#
# if __name__ == "__main__":
#     unittest.main()
