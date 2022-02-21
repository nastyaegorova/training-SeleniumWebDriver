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

def is_element_present (driver, *args):
    driver.find_element(*args)


    #return len(driver.find_elements(*args)) > 0

def test_example(driver):
    #driver.implicitly_wait(10)
    driver.get("http://localhost:8080/litecart/admin/login.php?redirect_url=%2Flitecart%2Fadmin%2F")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()

    list_ = driver.find_elements_by_css_selector("#box-apps-menu > li")


    for index in range(len(list_)):
        list_ = driver.find_elements_by_css_selector("#box-apps-menu > li")
        li = list_[index]
        li.find_element_by_css_selector("a").click()
        time.sleep(0.5)
        list_ = driver.find_elements_by_css_selector("#box-apps-menu > li")
        li = list_[index]
        docs = li.find_elements_by_css_selector("ul.docs > li > a")
        for i in range(len(docs)):
            docs[i].click()
            list_ = driver.find_elements_by_css_selector("#box-apps-menu > li")
            li = list_[index]
            docs = li.find_elements_by_css_selector("ul.docs > li > a")
            is_element_present(driver, By.TAG_NAME, 'h1')
            time.sleep(1)

