from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time


def test_login_podrygka():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()

    try:
        driver.get("https://www.podrygka.ru/")

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )

        user_icon = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".header-user.popup-menu"))
        )

        ActionChains(driver).move_to_element(user_icon).pause(1).perform()

        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-btn-login-enter]"))
        )
        driver.execute_script("arguments[0].click();", login_button)

        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='USER_LOGIN']"))
        )

        print("Форма входа открыта")

        username_field = driver.find_element(By.CSS_SELECTOR, "input[name='USER_LOGIN']")
        password_field = driver.find_element(By.CSS_SELECTOR, "input[name='USER_PASSWORD']")

        username_field.clear()
        username_field.send_keys("9851631234")

        password_field.clear()
        password_field.send_keys("Дщд20040306")

        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input[data-test-id='auth_enter_button']"))
        )

        print(f"Текст кнопки: {submit_button.get_attribute('value')}")

        print("Кликаем на кнопку входа...")
        driver.execute_script("arguments[0].click();", submit_button)

        print("Клик выполнен, ждем когда форма закроется...")

        WebDriverWait(driver, 20).until(
            EC.invisibility_of_element_located((By.CSS_SELECTOR, "input[name='USER_LOGIN']"))
        )

        print("Форма входа закрылась - тест пройден!")

        assert "podrygka.ru" in driver.current_url
        print(f"Текущий URL: {driver.current_url}")

    finally:
        time.sleep(2)
        driver.quit()

if __name__ == "__main__":
    test_login_podrygka()