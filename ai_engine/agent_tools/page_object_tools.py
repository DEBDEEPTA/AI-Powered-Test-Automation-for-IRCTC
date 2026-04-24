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

LoginPage:
Import: from pages.login_page import LoginPage
Methods:
- load_login_page(self)->None:
- login(self, name:str,password:str)->None:
- login_status(self,name:str)->bool:
LoginPage Rules:
- Dont include assertion to verify if url is redirecting to Dashboard
- use the login_status method to assert the login


Global Rules:
- Use Page Object Model classes.
- Avoid raw locators in generated tests.
- Do not perform real payment confirmation.
"""




