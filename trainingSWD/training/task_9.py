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

def test_example(driver):

    driver.get("http://localhost:8080/litecart/admin/?app=geo_zones&doc=geo_zones")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()

    rows = driver.find_elements_by_css_selector(".row")

    for i in range(len(rows)):
        columns = rows[i].find_elements_by_css_selector("td")
        columns[2].find_element_by_css_selector("a").click()

        rows1 = driver.find_elements_by_css_selector("#table-zones tr")
        zones = list()

        for index in range(1, len(rows1)-1):
            columns1 = rows1[index].find_elements_by_css_selector("td")
            get_value = columns1[2].find_element_by_css_selector('option[selected="selected"]').text
            zones.append(get_value)

        if zones != sorted(zones):
            raise Exception("Зоны расположены не в алфавитном порядке")

        driver.back()
        rows = driver.find_elements_by_css_selector(".row")


