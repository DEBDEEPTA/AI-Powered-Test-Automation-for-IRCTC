from utils.logger import get_logger
logger = get_logger()

def get_available_page_objects() -> str:
    """
    Returns available Page Object Model classes and methods.

    This helps the test generation agent generate tests using the
    existing Page Object Model instead of raw locators.
    """

    logger.info("Tool called: get_available_page_objects")

    return """
Available Page Object Classes:

==================================================
1. LoginPage
==================================================

Import:
from pages.login_page import LoginPage

Purpose:
LoginPage is used to load the IRCTC home/login page and perform login-related actions.

Methods:
- load_login_page() -> None
    Loads the IRCTC home page. This should be used as the first step in every generated test case.

- login(name: str, password: str) -> None
    Enters username and password and performs the login action.

- login_status(name: str) -> bool
    Returns True if login is successful for the given user name, otherwise returns False.

LoginPage Rules:
- Do not include assertion to verify whether the URL is redirected to Dashboard.
- Use login_status(name) method to assert login success.
- Do not write raw Playwright locators in generated tests.
- Do not hardcode real credentials unless the user explicitly provides them.
- If credentials are not provided, use placeholder values such as "username" and "password".


==================================================
2. SearchTrainsPage
==================================================

Import:
from pages.search_train_page import SearchTrainsPage

Purpose:
SearchTrainsPage is used to search trains from a source station to a destination station.

Methods:
- search_trains(
      source: str,
      destination: str,
      date: str = None,
      classes: str = None,
      general: str = None
  ) -> None
    Searches trains using source, destination, journey date, travel class, and quota/category.

- is_search_results_displayed() -> bool
    Returns True if train search results are displayed, otherwise returns False.

Parameter Details:
- source:
    Source station name or station code.
    Example: "KGP"

- destination:
    Destination station name or station code.
    Example: "YPR"

- date:
    Journey date.
    This parameter is optional.
    If the user provides a date, pass that value.
    If the user does not provide a date, pass None.

- classes:
    Travel class.
    This parameter is optional.
    If the user provides a class, pass that value.
    If the user does not provide a class, pass None.

- general:
    Quota/category.
    This parameter is optional.
    If the user provides a quota/category, pass that value.
    If the user does not provide a quota/category, pass None.

SearchTrainsPage Rules:
- Login is optional for train search.
- Default behavior: generate train search tests without login.
- If the user provides username and password, include login before searching trains.
- If the user does not provide username and password, do not call login().
- Always use search_trains() for train search scenarios.
- Use is_search_results_displayed() to assert that train search results are displayed.
- Do not invent extra SearchTrainsPage methods.
- Do not write raw Playwright locators in generated tests.

Example Usage Without Login:
login_page = LoginPage(page)
login_page.load_login_page()

search_page = SearchTrainsPage(page)
search_page.search_trains(
    source="KGP",
    destination="YPR",
    date=None,
    classes=None,
    general=None
)

assert search_page.is_search_results_displayed()

Example Usage With Login:
login_page = LoginPage(page)
login_page.load_login_page()
login_page.login("username", "password")
assert login_page.login_status("username")

search_page = SearchTrainsPage(page)
search_page.search_trains(
    source="KGP",
    destination="YPR",
    date=None,
    classes=None,
    general=None
)

assert search_page.is_search_results_displayed()


==================================================
Global Rules
==================================================

- Use only the available Page Object Model classes and methods listed above.
- Avoid raw Playwright locators in generated tests.
- Do not perform real payment confirmation.
- As the first step for every generated test case, use load_login_page() from LoginPage because it loads the home page.
- If a specific Page Object rule conflicts with a global rule, prioritize the specific Page Object rule.
- Do not invent methods that are not listed in this tool response.
- Keep generated tests readable and pytest-compatible.
"""




