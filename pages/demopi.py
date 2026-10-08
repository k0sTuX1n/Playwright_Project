from playwright.sync_api import Page


class Demopi:
    def __init__(self, page: Page):
        self.page = page
        self.username = page.get_by_placeholder("Username")
        self.password = page.get_by_placeholder("Password")
        self.loginn = page.get_by_role("button", name="Login")
        self.backpack = page.locator( "//button[@id='add-to-cart-sauce-labs-backpack']")

    def login(self, username, password):
        self.username.fill(username)
        self.password.fill(password)
        self.loginn.click()

    def backpacks(self):
        self.backpack.click()


         



