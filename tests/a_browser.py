from playwright.sync_api import Page , expect
from pages.browser_page import BrowserPag


def test_login(page , open_site):
    browser_page = BrowserPag(page)
    browser_page.login("visual_user", "secret_sauce")
    expect(page.get_by_text("Swag Labs")).to_be_visible()
    expect(page.get_by_text("Products")).to_be_visible()
    page.locator("#add-to-cart-sauce-labs-backpack").click()

def test_password(page , open_site):
    browser_page = BrowserPag(page)
    browser_page.login("visual_user", "secret_sauce")
    page.locator("#add-to-cart-sauce-labs-backpack").click()










    
    
    

    
   
    



    
   
   
#pytest --headed --slowmo 1000 