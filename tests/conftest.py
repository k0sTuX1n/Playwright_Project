import pytest
from playwright.sync_api import Page

@pytest.fixture
def open_site(page: Page):
    page.goto("https://www.play-qa.com")
    return page