import pytest
import time
from selenium import webdriver


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    #wd = webdriver.Firefox()
    #wd = webdriver.Edge()
    print(wd.capabilities)
    request.addfinalizer(wd.quit)
    return wd


def check_font_size (size):
    new_size = size[0:-2]
    return float(new_size)


def check_color (color: str):
    start_index = color.index("(")
    rgb = color[start_index + 1:-1].split(",")
    return int(rgb[0]), int(rgb[1]), int(rgb[2])


def test_example(driver):

    driver.get("http://localhost:8080/litecart/en/")

    duck = driver.find_element_by_css_selector("#box-campaigns .product")
    duck_name = duck.find_element_by_css_selector(".name")
    duck_name_text = duck_name.text
    duck_regular_price = duck.find_element_by_css_selector(".regular-price")
    regular_price_text = duck_regular_price.text
    duck_sale_price = duck.find_element_by_css_selector(".campaign-price")
    sale_price_text = duck_sale_price.text

    if duck_regular_price.value_of_css_property("text-decoration-line") != "line-through":
        raise Exception("Цена на главной странице не зачеркнута")

    color_gray = duck_regular_price.value_of_css_property("color")
    r, g, b = check_color(color_gray)

    if (r != g) and (g != b):
        raise Exception("Цвет обычной цены на главной странице не серый")

    if int(duck_sale_price.value_of_css_property("font-weight")) < 700:
        raise Exception("Акционная цена на главной странице не жирная")

    color_red = duck_sale_price.value_of_css_property("color")
    r1, g1, b1 = check_color(color_red)

    if not(r1 != 0 and ((g1, b1) == (0, 0))):
        raise Exception("Цвет акционной цены на главной странице не красный")

    font_size_regular = duck_regular_price.value_of_css_property("font-size")
    font_size_sale = duck_sale_price.value_of_css_property("font-size")

    if check_font_size(font_size_regular) >= check_font_size(font_size_sale):
        raise Exception("Обычная цена на главной странице имеет меньший или равный акционной размер шрифта")

    duck_name.click()

    prod_duck_name = driver.find_element_by_css_selector("h1[itemprop='name']")
    prod_duck_regular_price = driver.find_element_by_css_selector(".regular-price")
    prod_duck_sale_price = driver.find_element_by_css_selector(".campaign-price")

    if duck_name_text != prod_duck_name.text:
        raise Exception ("Не совпадает название товара")

    if regular_price_text != prod_duck_regular_price.text:
        raise Exception("Не совпадают обычные цены")

    if sale_price_text != prod_duck_sale_price.text:
        raise Exception("Не совпадают акционные цены")

    if prod_duck_regular_price.value_of_css_property("text-decoration-line") != "line-through":
        raise Exception("Цена на странице товара не зачеркнута")

    prod_color_gray = prod_duck_regular_price.value_of_css_property("color")
    r, g, b = check_color(prod_color_gray)

    if (r != g) and (g != b):
        raise Exception("Цвет обычной цены на странице товара не серый")

    if int(prod_duck_sale_price.value_of_css_property("font-weight")) < 700:
        raise Exception("Акционная цена на странице товара не жирная")

    prod_color_red = prod_duck_sale_price.value_of_css_property("color")
    r1, g1, b1 = check_color(prod_color_red)

    if not(r1 != 0 and ((g1, b1) == (0, 0))):
        raise Exception("Цвет акционной цены на странице товара не красный")

    prod_font_size_regular = prod_duck_regular_price.value_of_css_property("font-size")
    prod_font_size_sale = prod_duck_sale_price.value_of_css_property("font-size")

    if check_font_size(prod_font_size_regular) >= check_font_size(prod_font_size_sale):
        raise Exception("На странице товара обычная цена имеет больший или равный акционной размер шрифта")