from playwright.async_api import Page
import pytest


@pytest.fixture
def open_site(page):
    page.goto("https://www.saucedemo.com/")
    return page

@pytest.fixture
def open_site2(page):
    page.goto("https://practice.expandtesting.com/login?utm_source=chatgpt.com")
