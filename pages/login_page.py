from playwright.sync_api import Page, expect

class LoginPage:
    URL = "https://www.irctc.co.in/"

    def __init__(self, page:Page):
        self.page = page

    #LOCATORS
    LOGIN_REGISTER_BUTTON = "//a[text()=' LOGIN / REGISTER ']"
    USERNAME_INPUT_BOX = "//input[@placeholder='User Name']"
    PASSWORD_INPUT_BOX = "//input[@placeholder='Password']"
    SIGN_IN_BUTTON = "//button[text()='SIGN IN']"


    def load_login_page(self):
        """
         Load the Login page of IRCTC
        """
        self.page.goto(LoginPage.URL)
        self.page.set_viewport_size({"width": 1920, "height": 940})


    def login(self, name:str,password:str):
        """
            Logs in to IRCTC using the given username and password.

            This method performs the complete login flow:
            1. Clicks the Login/Register button.
            2. Locates the username and password input fields.
            3. Clears any existing values from both fields.
            4. Enters the provided username and password.
            5. Clicks the Sign In button to submit the login form.

            Args:
                name (str): The username, email, or mobile number used for login.
                password (str): The password associated with the given user account.

            Returns:
                None
        """

        self.page.locator(self.LOGIN_REGISTER_BUTTON).click()

        user_name = self.page.locator(self.USERNAME_INPUT_BOX)
        pass_word = self.page.locator(self.PASSWORD_INPUT_BOX)

        user_name.clear()
        user_name.fill(name)

        pass_word.clear()
        pass_word.fill(password)

        self.page.click(self.SIGN_IN_BUTTON)

    def login_status(self,name:str)->bool:
        """
        Checks whether the user login was successful.

        Returns:
            bool:
                True if the user is logged in successfully.
                False if the login fails or the logged-in state is not detected.
        """
        LOGGED_IN_USER_NAME = f"// span[contains(text(), '{name}')]"

        self.page.locator(LOGGED_IN_USER_NAME).wait_for(state="visible")
        logged_in_user_name = self.page.locator(LOGGED_IN_USER_NAME)
        return  logged_in_user_name.is_visible()


