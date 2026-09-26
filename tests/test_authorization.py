from playwright.sync_api import expect, Page
import pytest

@pytest.mark.regression
@pytest.mark.autorization
@pytest.mark.parametrize('email, password', [('user.name@gmail.com','password'), ('user.name@gmail.com','  '), ('  ','password')] )
def test_wrong_email_or_password_autorization(chromium_page: Page, email: str, password: str):
        chromium_page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

        email_input = chromium_page.get_by_test_id('login-form-email-input').locator(
            'input')  # находим локатор для email, вместо page.locator('//div[@data-testid="login-form-email-input"]//div//input') мы так же используем get_by_test_id, только еще говорим локатору, что найди элемент input, потому что test_id только в div, а нам нужно спуститься ниже
        email_input.fill(email)  # с помощью метода fill мы вводим адрес

        password_input = chromium_page.get_by_test_id('login-form-password-input').locator(
            'input')  # находим локатор для password
        password_input.fill(password)  # с помощью метода fill мы вводим пароль

        login_button = chromium_page.get_by_test_id(
            'login-page-login-button')  # вместо page.locator('//button[@data-testid="login-page-login-button"]')
        login_button.click()

        wrong_email_orpassword_alert = chromium_page.get_by_test_id('login-page-wrong-email-or-password-alert')
        expect(wrong_email_orpassword_alert).to_be_visible()  # ожидаем, что локатор будет визабл
        expect(wrong_email_orpassword_alert).to_have_text('Wrong email or password')

