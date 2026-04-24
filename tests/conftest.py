import os
from datetime import datetime
import pytest
from playwright.sync_api import sync_playwright


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):

    if hasattr(config.option, "htmlpath") and config.option.htmlpath:

        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        reports_dir = os.path.join(os.getcwd(), "reports")
        os.makedirs(reports_dir, exist_ok=True)

        config.option.htmlpath = os.path.join(reports_dir, f"API_Test_Report_{timestamp}.html")

# @pytest.fixture(scope="function")
# def page():
#     playwright =  sync_playwright().start()
#     browser = playwright.chromium.launch(headless=False)
#     context = browser.new_context()
#
#     page = context.new_page()
#
#     return page

@pytest.fixture(scope="function")
def page():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()

        page = context.new_page()

        yield page

        context.close()
        browser.close()