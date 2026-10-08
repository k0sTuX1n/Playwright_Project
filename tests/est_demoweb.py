from playwright.sync_api import Page
from pages.demo_web import Demoweb
import pytest


@pytest.mark.parametrize(
    "username,password",
    [
        ("user1@mail.com", "123"),
        ("user2@mail.com", "456"),
        ("user3@mail.com", "789"),
    ]
)


def test_demoweb(open_site , page:Page , username,password):
    demo = Demoweb(page)
    demo.login(username,password)
    demo.open_books()
    demo.add_to_cart_button()


    
    

    


    