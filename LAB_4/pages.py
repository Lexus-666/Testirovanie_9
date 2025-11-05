from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def is_element_present(self, locator, timeout=3):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            return True
        except:
            return False

    def click(self, locator):
        self.find(locator).click()

    def type(self, locator, text):
        element = self.find(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        return self.find(locator).text


class PracticeFormPage(BasePage):
    URL = "https://demoqa.com/automation-practice-form"

    FIRST_NAME = (By.ID, "firstName")
    LAST_NAME = (By.ID, "lastName")
    EMAIL = (By.ID, "userEmail")
    GENDER_MALE = (By.XPATH, "//label[@for='gender-radio-1']")
    MOBILE = (By.ID, "userNumber")
    SUBMIT = (By.ID, "submit")
    MODAL_TITLE = (By.ID, "example-modal-sizes-title-lg")

    def open(self):
        self.driver.get(self.URL)

    def fill_form(self, first, last, email, mobile):
        self.type(self.FIRST_NAME, first)
        self.type(self.LAST_NAME, last)
        self.type(self.EMAIL, email)
        self.click(self.GENDER_MALE)
        self.type(self.MOBILE, mobile)

    def submit(self):
        self.driver.execute_script("arguments[0].click();", self.find(self.SUBMIT))

    def get_modal_title(self):
        return self.get_text(self.MODAL_TITLE)

    def is_modal_displayed(self):
        return self.is_element_present(self.MODAL_TITLE)