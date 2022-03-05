import pytest
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import uuid


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    print(wd.capabilities)
    request.addfinalizer(wd.quit)
    return wd

def test_example(driver):

    driver.get("http://localhost:8080/litecart/en/")
    driver.find_element_by_css_selector("#box-account-login [href='http://localhost:8080/litecart/en/create_account']").click()

    driver.find_element_by_css_selector("input[name='firstname']").send_keys("first_name")
    driver.find_element_by_css_selector("input[name='lastname']").send_keys("last_name")
    driver.find_element_by_css_selector("input[name='address1']").send_keys("address1")
    driver.find_element_by_css_selector("input[name='postcode']").send_keys("12345")
    driver.find_element_by_css_selector("input[name='city']").send_keys("city")

    element = driver.find_element_by_css_selector("select[name='country_code']")
    select = Select(element)
    select.select_by_visible_text("United States")

    uid = str(uuid.uuid4())
    email = uid[0:10]+"@mail.ru"
    driver.find_element_by_css_selector("input[name='email']").send_keys(email)

    driver.find_element_by_css_selector("input[name='phone']").send_keys("89999999999")

    driver.find_element_by_css_selector("input[name='password']").send_keys("123")
    driver.find_element_by_css_selector("input[name='confirmed_password']").send_keys("123")

    driver.find_element_by_css_selector("button[name='create_account']").click()

    driver.find_element_by_css_selector("#box-account [href='http://localhost:8080/litecart/en/logout']").click()

    driver.find_element_by_css_selector("input[name='email']").send_keys(email)
    driver.find_element_by_css_selector("input[name='password']").send_keys("123")
    driver.find_element_by_css_selector("button[name='login']").click()

    driver.find_element_by_css_selector("#box-account [href='http://localhost:8080/litecart/en/logout']").click()





