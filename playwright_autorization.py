from playwright.sync_api import sync_playwright, expect


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

    email_input = page.get_by_test_id('login-form-email-input').locator('input') #находим локатор для email, вместо page.locator('//div[@data-testid="login-form-email-input"]//div//input') мы так же используем get_by_test_id, только еще говорим локатору, что найди элемент input, потому что test_id только в div, а нам нужно спуститься ниже
    email_input.fill('user.name@gmail.com') #с помощью метода fill мы вводим адрес

    password_input = page.get_by_test_id('login-form-password-input').locator('input') #находим локатор для password
    password_input.fill('password') #с помощью метода fill мы вводим пароль

    login_button = page.get_by_test_id('login-page-login-button') # вместо page.locator('//button[@data-testid="login-page-login-button"]')
    login_button.click()

    wrong_email_orpassword_alert = page.get_by_test_id('login-page-wrong-email-or-password-alert')
    expect(wrong_email_orpassword_alert).to_be_visible() #ожидаем, что локатор будет визабл
    expect(wrong_email_orpassword_alert).to_have_text('Wrong email or password')

    page.wait_for_timeout(5000)

