import pytest
import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome(executable_path="D:\\chromedriver.exe")
    print(wd.capabilities)
    request.addfinalizer(wd.quit)
    return wd


def test_example(driver):
    driver.get("http://localhost:8080/litecart/admin/login.php?redirect_url=%2Flitecart%2Fadmin%2F")
    driver.find_element_by_name("username").send_keys("nastyaegorova")
    driver.find_element_by_name("password").send_keys("123")
    driver.find_element_by_name("remember_me").click()
    driver.find_element_by_name("login").click()
