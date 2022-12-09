from time import sleep
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
# from pars_wb.settings import service
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from app.bot import logger

from pars_wb.constants import PAUSE_DURATION_SECONDS, ERROR_SEARCHE_MESSAGE, LOG_DEBAG_PARS_ELEMENT

URL = os.getenv("URL")


def get_product(articul, product):
    # driver = webdriver.Chrome(service=service)
    driver = webdriver.Remote(
        "http://selenium:4444/wd/hub",
        desired_capabilities=DesiredCapabilities.CHROME,
    )
    driver.get(URL)
    driver.maximize_window()
    sleep(PAUSE_DURATION_SECONDS)
    try:
        search_input = driver.find_element(
            By.XPATH, '//div[@class="search-catalog__block"]/input'
        )
    except NoSuchElementException as error:
        logger.critical(f"{LOG_DEBAG_PARS_ELEMENT}. {error}")
    search_input.click()
    search_input.send_keys(product)
    search_input.send_keys(Keys.ENTER)

    sleep(PAUSE_DURATION_SECONDS)
    count_page = 0
    for p in range(101):
        try:
            count_page += 1
            card = driver.find_element(
                By.XPATH,
                (
                    '//div[@class="product-card-list"]'
                    f'//div[@data-popup-nm-id={articul}]'
                ),
            )
            item_number = card.get_attribute("data-card-index")
            card.click()
            if count_page <= 100:
                return (f"Ваш товар находится на странице №{count_page}, "
                        f"на позиции №{int(item_number) + 1}")
            else:
                return ERROR_SEARCHE_MESSAGE
        except NoSuchElementException:
            next_page = driver.find_element(
                By.XPATH, '//a[@class="pagination-next pagination__next"]'
            )
            next_page.click()
        sleep(PAUSE_DURATION_SECONDS)
    driver.quit()
