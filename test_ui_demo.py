import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException


@pytest.fixture(scope="module")
def driver():
    """Инициализирует браузер Chrome и открывает demoqa.com."""
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://demoqa.com")
    print(f"Opened URL: {driver.current_url}")  # Логируем текущий URL
    print(f"Initial title: {driver.title}")  # Логируем заголовок
    yield driver
    driver.quit()


def test_site_title(driver):
    """Проверяет, что заголовок страницы содержит 'DEMOQA'."""
    try:
        WebDriverWait(driver, 10).until(EC.title_contains("DEMOQA"))
        print(f"Page title after wait: {driver.title}")  # Логируем заголовок после ожидания
        assert "DEMOQA" in driver.title
    except TimeoutException:
        pytest.fail(f"Title did not load within 10 seconds. Current title: {driver.title}")


def test_logo_present(driver):
    """Проверяет, что логотип виден на странице."""
    try:
        logo = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'img[src*="Toolsqa"]'))
        )
        assert logo.is_displayed()
    except (NoSuchElementException, TimeoutException):
        pytest.fail("Logo not found or not visible within 10 seconds")
