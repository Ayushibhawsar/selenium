from lib2to3.pgen2 import driver

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from loginpage import *
class SkipPage(GoibiboBooking):
    def __init__(self, driver):
        GoibiboBooking.__init__(self, driver)
        self.driver = driver
        self.driver.get('https://www.goibibo.com/')

    def skip_button(self):
        self.driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[1]/div/div/div/div/div[2]/p[2]')
        skip_button = WebDriverWait(driver, 20).until(self.login())
        skip_button.click()
