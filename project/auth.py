from playwright.sync_api import Playwright, sync_playwright


def login_and_save_cookie(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    content = browser.new_context()
    page = content.new_page()

    page.goto('https://quotes.toscrape.com/')
    page.get_by_text(text='Login').click()

    # авторизация
    page.fill('input[name="username"]', 'Dias')
    page.fill('input[name="password"]', '43322')
    page.click("input[type='submit']")
    content.storage_state(path='state.json')

with sync_playwright() as p:
    login_and_save_cookie(p)