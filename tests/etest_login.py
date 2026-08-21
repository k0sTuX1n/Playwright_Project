from playwright.sync_api import Page, expect
from pages.login_page import LoginPage


def test_login(page , open_site: Page):
    login_page = LoginPage(page)
    login_page.login("visual_user", "secret_sauce")
    expect(page.get_by_text("Swag Labs")).to_be_visible()
    