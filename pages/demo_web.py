from playwright.sync_api import Page 

class Demoweb:
    def __init__(self, page : Page):
        self.page = page 
        self.log_in = page.get_by_role("link" , name=("Log in"))
        self.email = page.get_by_label("Email:")
        self.password = page.locator("#Password")
        self.button = page.get_by_role("button",name=("Log in"))
        self.books = page.get_by_role("link",name=("Books"))
        self.add_to_cart = page.locator('//input[@value="Add to cart"]')


    def login(self , username , password):
        self.log_in.click()
        self.email.fill(username)
        self.password.fill(password)
        self.button.click()

    def open_books(self):
        self.books.nth(1).click()

    def add_to_cart_button(self):
        self.add_to_cart.nth(2).click()
        



        


