import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    print(wd.capabilities)
    request.addfinalizer(wd.quit)
    return wd

def check_stickers (list_):
    for index in range(len(list_)):
        li = list_[index]
        if len(li.find_elements_by_css_selector("div.sticker")) != 1:
            raise Exception("У утки не один стикер")

def test_example(driver):

    driver.get("http://localhost:8080/litecart/en/")

    list_popular = driver.find_elements_by_css_selector("div#box-most-popular ul > li")
    list_campaigns = driver.find_elements_by_css_selector("div#box-campaigns ul > li")
    list_latest = driver.find_elements_by_css_selector("div#box-latest-products ul > li")

    check_stickers(list_popular)
    check_stickers(list_campaigns)
    check_stickers(list_latest)