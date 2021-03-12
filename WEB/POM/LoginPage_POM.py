
class LoginPage:

    passwordField = '//*[@id="password"]'
    loginButton = '//*[@id="customer_login"]/div[1]/form/p[3]/button'
    logoutButton = '//*[@id="post-1537"]/div/div/div/div/section[2]/div/div/div[4]/div/div/div/div/div/div[1]/a/i'
    confirmLogout = '//*[@id="post-1537"]/div/div/div/div/section[3]/div/div/div/div/div/div/div/div/div/div/div/div/a'
    displayName = '//*[@id="account_display_name"]'
    loginErrorMessage = '//*[@id="post-1537"]/div/div/div/div/section[3]/div/div/div/div/div/div/div/div/div/div[1]/ul/li'
    userNameField = '//*[@id="username"]'

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element_by_xpath(self.userNameField).clear()
        self.driver.find_element_by_xpath(self.userNameField).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element_by_xpath(self.passwordField).clear()
        self.driver.find_element_by_xpath(self.passwordField).send_keys(password)

    def clickLogin(self):
        self.driver.find_element_by_xpath(self.loginButton).click()

    def clickLogout(self):
        self.driver.find_element_by_xpath(self.logoutButton).click()

    def clickConfirm(self):
        self.driver.find_element_by_xpath(self.confirmLogout).click()
