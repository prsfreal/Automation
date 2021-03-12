import pytest
from selenium.webdriver.common.action_chains import ActionChains
from decouple import config

from WEB.POM.ArticlesArchivePage_POM import ArticleArchivePage
from WEB.POM.ArticlePage_POM import ArticlePage
from UTILITIES.BasicClassConfig import basic
from UTILITIES.PassParameters import PassParameters
from WEB.DATA.ArticlePage_Data import TestData


class Test_HomePageSuite(basic):
    URL = config('vsarchive')

    #This fixture sets up and driver, goes to initial URL of test, initiates ActionChains,
    # and initializes the POM class(es) for the tests
    @pytest.fixture
    def additionalsetup(self, setupbrowser):
        self.driver = setupbrowser
        self.driver.get(self.URL)
        self.action = ActionChains(self.driver)
        self.aap = ArticleArchivePage(self.driver)
        self.ap = ArticlePage(self.driver)

    @pytest.mark.parametrize("email, password",
                             PassParameters.parseParamaters(TestData.para_01_twitter_login))
    def test_twitterLogin(self, email, password, additionalsetup):
        self.logger.info(f'***{self.defName}: test_0001: Send a tweet***')
        self.aap.navigateToArticle1()

        self.waitAndsee(self.ap.twitterwidget)
        self.ap.navigateToTwitter()
        window1 = self.driver.window_handles[1]
        self.driver.switch_to_window(window1)
        self.logger.info('Now in second window')

        self.waitAndsee(self.ap.tweetfield)
        self.ap.signIntoTwitter(email, password)
        self.logger.info('Signed into twitter but did not send the tweet. Just requires one more command.')


    @pytest.mark.parametrize("email, password",
                             PassParameters.parseParamaters(TestData.para_02_discount))
    def test_discountSignUp(self, email, password, additionalsetup):
        self.logger.info(f'***{self.defName}: test_0002: Sign up for discount***')

        self.aap.navigateToArticle1()

        self.waitAndsee(self.ap.discountname)
        self.ap.discountSubmit(email, password)

        self.waitAndsee(self.ap.discountverifypath)
        self.src = self.driver.page_source

        assert self.ap.discountverifytext in self.src, self.logger.info('Could not find verify text.')
        self.logger.info('PASSED')



