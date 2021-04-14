import pytest
from pytest import fixture
from selenium import webdriver
from unittest import TestCase
class GoibiboBooking():
    def __init__(self, driver):
        self.driver = driver
        self.driver.get('https://www.goibibo.com/')

    def user_login(self, mobile_no):
        self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/header/div/div/div/p').click()
        login_field = self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div/div[1]/form/div/input')
        login_field.send_keys(mobile_no)
        continue_button = self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div/div[1]/input')
        continue_button.click()
        self.enter_otp()
        self.driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[1]/div/div/div/span/span').click()
        self.travel_booking()

    def login(self):
        self.user_login('9981140654')


    def enter_otp(self):
        l = ['//*[@id="root"]/div[2]/div[1]/div/div/div[2]/div/div[1]/div[1]/div[1]/input',
             '//*[@id="root"]/div[2]/div[1]/div/div/div[2]/div/div[1]/div[1]/div[2]/input',
             '//*[@id="root"]/div[2]/div[1]/div/div/div[2]/div/div[1]/div[1]/div[3]/input',
             '//*[@id="root"]/div[2]/div[1]/div/div/div[2]/div/div[1]/div[1]/div[4]/input']
        otp = input('enter otp: ')
        otp_list = list(otp)
        for index, field in enumerate(l):
            self.driver.find_element_by_xpath(field).send_keys(otp_list[index])


    def from_city(self, from_city):
        # from_field = self.driver.find_element_by_value('Mumbai (BOM)')
        # from_field.click()
        # exit()
        from_field = self.driver.find_element_by_xpath('//*[@id="gosuggest_inputSrc"]')
        from_field.click()
        from_field.send_keys(from_city)
        self.driver.find_element_by_xpath('//*[@id="gosuggest_inputSrc"]').click()

        
    def destination_city(self, destination_city):
        destination_field = self.driver.find_element_by_xpath('//*[@id="gosuggest_inputDest"]')
        destination_field.click()
        destination_field.send_keys(destination_city)
        self.driver.find_element_by_xpath('//*[@id="gosuggest_inputDest"]').click()

    def departure_time(self):
        # self.driver.find_element_by_xpath('//*[@id="departureCalendar"]').send_keys('20210412')
        # exit()
        self.driver.find_element_by_xpath('//*[@id="departureCalendar"]').click()
        departure_field = self.driver.find_element_by_xpath('//*[@id="fare_20210412"]')
        departure_field.click()

    def return_time(self):
        self.driver.find_element_by_xpath('//*[@id="returnCalendar"]').click()
        return_field = self.driver.find_element_by_xpath('//*[@id="fare_20210413"]')
        return_field.click()
        # self.driver.find_element_by_xpath('//*[@id="pax_link_common"]').click()
        # traveller_category = self.driver.find_element_by_xpath('//*[@id="pax_link_common"]/div/ul/li[2]/div/i').click()

    def submit_search(self):
        search = self.driver.find_element_by_xpath('//*[@id="gi_search_btn"]')
        search.click()

    def travel_booking(self):
       self.from_city('Mumbai, India (BOM)')
       self.destination_city('Jaipur, India (JAI)')
       self.departure_time()
       self.return_time()
       self.submit_search()

goibibobooking = GoibiboBooking(webdriver.Chrome())
goibibobooking.login()

