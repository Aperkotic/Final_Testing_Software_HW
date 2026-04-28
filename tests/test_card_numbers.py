import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def test_card_numbers(driver):
    driver.get('http://localhost:8000/?balance=30000&reserved=20001')
    wait = WebDriverWait(driver, 10)

    button_ruble = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@role='button'][1]")))
    button_ruble.click()

    card_number = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='0000 0000 0000 0000']")))
    card_number.clear()
    card_number.send_keys('12345678123456781')

    transfer_button = wait.until(EC.presence_of_element_located((By.XPATH, "//span [@class='g-button__text']")))

    assert not transfer_button.is_displayed()