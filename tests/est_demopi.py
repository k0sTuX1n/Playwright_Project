from playwright.sync_api import Page
from pages.demopi import Demopi


def test_demopi(page: Page):
    page.goto("https://www.saucedemo.com/")

    demo = Demopi(page)

    demo.login("standard_user", "secret_sauce")
    demo.backpacks()
    
    
   

    
