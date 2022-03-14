import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    print(wd.capabilities)
    request.addfinalizer(wd.quit)
    return wd


def test_example(driver):

    driver.get("http://localhost:8080/litecart/admin/?app=countries&doc=countries")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()

    driver.find_element_by_css_selector(".button").click()

    cur_window = driver.current_window_handle
    all_links = driver.find_elements_by_css_selector(".fa-external-link")

    for link in all_links:

        link.click()

        new_window = [i for i in driver.window_handles if i != cur_window]

        wait = WebDriverWait(driver, 10)
        wait.until(EC.new_window_is_opened(new_window))

        driver.switch_to.window(new_window[0])
        driver.close()
        driver.switch_to.window(cur_window)