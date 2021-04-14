import pytest
from selenium import webdriver

def test_first_case_with_selenium_pytest():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://www.google.com')
    assert "Google" == driver.title

class Test_GoibiboBooking():
    @pytest.mark.parametrize("url", ['https://www.goibibo.com/'])
    def test_goibibo_url
