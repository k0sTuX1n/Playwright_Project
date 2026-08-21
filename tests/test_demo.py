from playwright.sync_api import Page 
from pages.demo import DemoDemo 

def test_demoo(page:Page):
    page.goto("https://www.saucedemo.com/?utm_source=chatgpt.com")
    demo=DemoDemo(page)
    demo.login("error_user" , "secret_sauce")
    demo.add_products()
    demo.go_to_checkout()
    



