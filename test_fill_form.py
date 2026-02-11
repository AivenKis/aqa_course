import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()  # 1. Открыли «дверь» в интернет
    yield driver  # 2. Дали ключи всем тестам
    driver.quit()  # 3. Закрыли дверь после работы


def test_fill_text_box(driver):
    # 1. Заходим в приёмную
    driver.get("https://demoqa.com/text-box")

    # 2. Находим строку «Ф.И.О.» и пишем «Alice»
    name_field = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "userName"))
    )
    name_field.send_keys("Alice")  # 🖋️ «пишем»

    # 3. Находим строку «E-mail» и пишем «alice@mail.com»
    email_field = driver.find_element(By.ID, "userEmail")
    email_field.send_keys("alice@mail.com")

    # 4. Находим кнопку «Отправить» и нажимаем
    submit_btn = driver.find_element(By.ID, "submit")
    submit_btn.click()  # 👆 «отдаём анкету»

    # 5. Ждём, пока появится доска объявлений
    output = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "output"))
    )

    # 6. Проверяем, что там написано «Name:Alice»
    assert "Name:Alice" in output.text  # ✅ «секретарь всё записал»
