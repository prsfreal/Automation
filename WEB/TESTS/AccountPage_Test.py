import pytest
from decouple import config
from selenium.webdriver.common.action_chains import ActionChains

from WEB.DATA.AccountsPage_Data import TestData
from WEB.POM.HomePage_POM import HomePage
from WEB.POM.LoginPage_POM import LoginPage
from UTILITIES.BasicClassConfig import basic
from UTILITIES.PassParameters import PassParameters


class Test_Login(basic):
    URL = config('vshome')


    #This fixture sets up and driver, goes to initial URL of test, initiates ActionChains,
    # and initializes the POM class(es) for the tests

    @pytest.fixture
    def additionalsetup(self, setupbrowser):
        self.driver = setupbrowser
        self.driver.get(self.URL)
        self.action = ActionChains(self.driver)
        self.hp = HomePage(self.driver)
        self.lp = LoginPage(self.driver)

    @pytest.mark.parametrize("ids, password",
                             PassParameters.parseParamaters(TestData.para_01_Successful_Login))
    def test_01_Successful_Login(self, ids, password, additionalsetup):
        self.logger.info(f'***{self.defName}: Login to Account and Logout***')

        #Start of Test
        self.hp.navigateToAccountPage()

        #Login
        self.waitAndsee(LoginPage.userNameField)
        self.lp.setUserName(ids)
        self.lp.setPassword(password)
        self.lp.clickLogin()

        #Logout step 1
        self.waitAndsee(self.lp.logoutButton)
        self.lp.clickLogout()

        #Logout step 2
        self.waitAndsee(self.lp.confirmLogout)
        self.lp.clickConfirm()

        #Successful logout validation
        assert self.driver.title == 'My Account | Validate Services', self.logger.info(f'Title = {self.driver.title} != My Account | Validate Services')
        self.logger.info('PASSED')

