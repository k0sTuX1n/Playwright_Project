from playwright.sync_api import Page


class DemoDemo:
    def __init__(self, page: Page):
            self.page = page

            self.username=page.get_by_placeholder("Username")
            self.password=page.get_by_placeholder("Password")
            self.loginbutton=page.locator("#login-button")

            self.backpack = page.locator("#add-to-cart-sauce-labs-backpack")
            self.onesie = page.locator("#add-to-cart-sauce-labs-onesie")
            self.bike_light = page.locator("#add-to-cart-sauce-labs-bike-light")

            self.shopping_cart = page.locator('[data-test="shopping-cart-link"]')
            self.checkout = page.get_by_role("button", name="Checkout")

    def login(self,username,password):
         self.username.fill(username)
         self.password.fill(password)
         self.loginbutton.click()

    def add_products(self):
         products = [
         self.backpack,
         self.onesie,
         self.bike_light
         ]

         for product in products:
          product.click()


    def go_to_checkout(self):
         self.shopping_cart.click()
         self.checkout.click()

         

        

