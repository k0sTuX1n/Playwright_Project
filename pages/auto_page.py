from playwright.sync_api import Page 

class Auto_page:
    def __init__(self,page:Page):
        self.page = page
        self.username = page.get_by_label("username")
        self.password = page.get_by_label("password")
        self.submit_login = page.locator("#submit-login")
        self.test_cases = page.get_by_role("link",name=("Test Cases"))
        self.read_more = page.get_by_role("link",name=("Read More"))




    def login(self,username,password):
        self.username.fill(username)
        self.password.fill(password)
        self.submit_login.click()

    def link (self):
        self.test_cases.click()
        self.read_more.first.click()
        







        


