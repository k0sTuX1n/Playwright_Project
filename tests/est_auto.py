from playwright.sync_api import Page 
from pages.auto_page import Auto_page

def test_auto_а (page,open_site2):
    auto_pages = Auto_page(page)
    auto_pages.login("practice" , "SuperSecretPassword!")
    auto_pages.link()



    
    

    





