from playwright.sync_api import Page, expect, sync_playwright
import time

URL = "https://ecommerce-playground.lambdatest.io/"
class Register:
    def __init___(self, page:Page):
        self.page = page

    def test_create_account():
        page.goto(URL)
        page.locator("span:has-text('My account')").click()
        time(5)

if __name__ == '__main__':
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        regiter = Register(page)
        regiter.test_create_account()
        browser.close()