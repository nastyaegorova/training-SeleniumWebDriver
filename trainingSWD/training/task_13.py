import pytest
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    print(wd.capabilities)
    request.addfinalizer(wd.quit)
    return wd


def is_element_present(driver, locator):
    return len(driver.find_elements_by_css_selector(locator)) > 0


def test_example(driver):

    driver.get("http://localhost:8080/litecart/en/")

    for i in range(3):
        driver.find_element_by_css_selector("#box-most-popular .product").click()

        if is_element_present(driver, ".options"):
            element = driver.find_element_by_css_selector("select[name='options[Size]']")
            select = Select(element)
            select.select_by_visible_text("Small")

        driver.find_element_by_css_selector("button[name='add_cart_product']").click()

        wait = WebDriverWait(driver, 10)
        count = str(i + 1)
        wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, 'quantity'), count))

        driver.back()

    driver.find_element_by_css_selector("#cart").click()

    while len(driver.find_elements_by_css_selector("button[name='remove_cart_item']")) != 0:
        table = driver.find_element_by_css_selector(".dataTable")
        driver.find_element_by_css_selector("button[name='remove_cart_item']").click()
        wait.until(EC.staleness_of(table))

    assert driver.find_element_by_css_selector("#checkout-cart-wrapper p").text == "There are no items in your cart."
