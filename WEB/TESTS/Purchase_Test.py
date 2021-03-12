import pytest
from selenium.webdriver.common.action_chains import ActionChains

from WEB.DATA.Purchase_Data import TestData
from WEB.POM.ArticlesArchivePage_POM import ArticleArchivePage
from WEB.POM.ArticlePage_POM import ArticlePage
from WEB.POM.CriminalBackgroundCheck_POM import CriminalBackgroundCheckPage
from WEB.POM.FederalLanding_POM import federalLandingPage
from WEB.POM.FederalCheckout_POM import FederalCheckoutPage
from UTILITIES.BasicClassConfig import basic
from UTILITIES.PassParameters import PassParameters
from decouple import config



class Test_HomePageSuite(basic):
    URL = config('vsarchive')

    #This fixture sets up and driver, goes to initial URL of test, initiates ActionChains,
    # and initializes the POM class(es) for the tests
    @pytest.fixture
    def additionalSetup(self, setupbrowser):
        self.driver = setupbrowser
        self.driver.get(self.URL)
        self.action = ActionChains(self.driver)
        self.aap = ArticleArchivePage(self.driver)
        self.ap = ArticlePage(self.driver)
        self.cbc = CriminalBackgroundCheckPage(self.driver)
        self.fl = federalLandingPage(self.driver)
        self.fc = FederalCheckoutPage(self.driver)

    @pytest.mark.parametrize("user",
                             PassParameters.parseParamaters(TestData.para_make_a_purchase))
    def test_0001(self, user, additionalSetup):
        self.logger.info(f'***{self.defName}: test_0001: Purchase BackgroundCheck***')
        self.aap.navigateToArticle1()

        self.waitAndsee(self.ap.backgroundcheckbutton)
        self.ap.navigateToBackgroundCheck()

        self.waitAndsee(self.cbc.federalCourtButton)
        self.cbc.navigateToFederalCourt()

        self.waitAndsee(self.fl.startreportbutton)
        self.fl.navigateToPurchase()

        self.waitAndsee(self.fc.orderfirstname)
        self.fc.makePurchase(user)

        self.waitAndsee(self.fc.addonorderbutton, 'XPATH', 60)
        self.logger.info(f'PASSED')


