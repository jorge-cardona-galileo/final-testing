from playwright.sync_api import Page, expect, sync_playwright
import time
import random
import string

URL = "https://ecommerce-playground.lambdatest.io/"


def generate_random_email():
    local_part_length = random.randint(5, 15)  # Random length between 5 and 15 characters
    local_part = ''.join(random.choices(string.ascii_lowercase + string.digits, k=local_part_length))
    domain_length = random.randint(4, 10)  # Random length between 4 and 10 characters
    domain = ''.join(random.choices(string.ascii_lowercase, k=domain_length))
    tlds = ['com', 'net', 'org']
    tld = random.choice(tlds)
    email = f"{local_part}@{domain}.{tld}"
    return email

class Register:
    def __init__(self, page: Page):
        self.page = page
    
    def wait_for_page_load(self, seconds=2):
        self.page.wait_for_load_state("networkidle")
        time.sleep(seconds) #Tiempo de espera para asegurar que la página se haya cargado completamente

    def test_create_account(self):
        self.page.goto(URL)
        self.wait_for_page_load()
        self.page.locator("span:has-text('My account')").nth(1).click()
        self.wait_for_page_load()
        self.page.locator("a:has-text('Continue')").click()
        self.wait_for_page_load()
        page.fill('input[name="firstname"]', "Jorge")
        page.fill('input[name="lastname"]', "Cardona")
        page.fill('input[name="email"]', generate_random_email())
        page.fill('input[name="telephone"]', "+50254588888")
        page.fill('input[name="password"]', "Fake_password1")
        page.fill('input[name="confirm"]', "Fake_password1")
        page.check('input[type="checkbox"]#input-agree')
        page.click('button[type="submit"]')
        self.wait_for_page_load()
        expect(page.locator("span:has-text('Your Account Has Been Created!')")).to_be_visible()
    
if __name__ == '__main__':
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        register = Register(page)
        register.test_create_account()
        browser.close()