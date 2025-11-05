from pages import PracticeFormPage

# Позитивный тест
def test_practice_form_success(driver):
    page = PracticeFormPage(driver)
    page.open()
    page.fill_form("Alexey", "Shilov", "X@test.com", "1234567890")
    page.submit()
    assert "Thanks for submitting the form" in page.get_modal_title()

# Негативный тест
def test_practice_form_empty_field(driver):
    page = PracticeFormPage(driver)
    page.open()
    page.submit()
    assert not page.is_modal_displayed(), "Модальное окно не должно появляться при пустой форме"