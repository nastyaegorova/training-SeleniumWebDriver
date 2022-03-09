import pytest
import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import uuid

@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    print(wd.capabilities)
    request.addfinalizer(wd.quit)
    return wd

def test_example(driver):

    driver.get("http://localhost:8080/litecart/admin/?app=catalog&doc=catalog")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()

    time.sleep(0.5)

    driver.find_element_by_css_selector("a[href='http://localhost:8080/litecart/admin/?category_id=0&app=catalog&doc=edit_product']").click()
    uid = str(uuid.uuid4())
    driver.find_element_by_css_selector("input[name='name[en]']").send_keys(uid)
    driver.find_element_by_css_selector("input[name='code']").send_keys("code")
    driver.find_element_by_css_selector("input[name='product_groups[]'][value='1-1']").click()
    driver.find_element_by_css_selector("input[name='quantity']").clear()
    driver.find_element_by_css_selector("input[name='quantity']").send_keys("100")
    file = os.path.abspath(os.path.curdir) + "\\source\\123.png"

    driver.find_element_by_css_selector("input[type='file']").send_keys(file)
    driver.find_element_by_css_selector("input[name='date_valid_from']").send_keys(Keys.HOME + "02.03.2021")
    driver.find_element_by_css_selector("input[name='date_valid_from']").send_keys(Keys.HOME + "02.03.2022")

    driver.find_element_by_css_selector(".index li a[href='#tab-information']").click()

    element = driver.find_element_by_css_selector("select[name='manufacturer_id']")
    select = Select(element)
    select.select_by_visible_text("ACME Corp.")

    driver.find_element_by_css_selector("input[name='keywords']").send_keys("keywords")
    driver.find_element_by_css_selector("input[name='short_description[en]']").send_keys("short")
    driver.find_element_by_css_selector(".trumbowyg-editor").send_keys("short")
    driver.find_element_by_css_selector("input[name='head_title[en]']").send_keys("head")
    driver.find_element_by_css_selector("input[name='meta_description[en]']").send_keys("meta")

    driver.find_element_by_css_selector(".index li a[href='#tab-prices']").click()

    element = driver.find_element_by_css_selector("select[name='purchase_price_currency_code']")
    select = Select(element)
    select.select_by_visible_text("Euros")

    driver.find_element_by_css_selector("input[name='purchase_price']").clear()
    driver.find_element_by_css_selector("input[name='purchase_price']").send_keys("100")

    driver.find_element_by_css_selector("input[name='prices[USD]']").send_keys("100")
    driver.find_element_by_css_selector("input[name='prices[EUR]']").send_keys("100")

    driver.find_element_by_css_selector("button[name='save']").click()

    driver.find_element_by_css_selector("input[name='query']").send_keys(uid + Keys.ENTER)
    link = driver.find_element_by_link_text(uid)
    index = driver.find_element_by_css_selector(".footer td").text
    if not(index == "Products: 1" and link.text == uid):
        raise Exception("Созданный продукт не найден")


