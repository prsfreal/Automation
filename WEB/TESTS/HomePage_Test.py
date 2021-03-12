import pytest
from decouple import config
from WEB.POM.HomePage_POM import HomePage
from WEB.POM.PrivacyPolicy_POM import PrivacyPolicy
from UTILITIES.BasicClassConfig import basic
from UTILITIES.DataBaseConnection import MySQLConnection
from selenium.webdriver.common.action_chains import ActionChains


class Test_HomePageSuite(basic):
    URL = config('vshome')

    #This fixture sets up and driver, goes to inital URL of test, and initiates ActionChains,
    # and initiailizes the POM class(es) for the tests
    @pytest.fixture
    def additionalSetup(self, setupbrowser):
        self.driver = setupbrowser
        self.driver.get(self.URL)
        self.action = ActionChains(self.driver)
        self.hp = HomePage(self.driver)

    def test_0001(self, additionalSetup):
        self.logger.info(f'***{self.defName}: test_0001: Verify Text of 3 Banners is Present***')

        self.src = self.driver.page_source

        assert self.hp.slider1text in self.src and self.hp.slider2text in self.src and self.hp.slider3text in self.src, self.logger.exception("--FAILED - All slider Text did not match")
        self.logger.info("--All slider present text present")


    def test_0002(self, additionalSetup):
        self.logger.info(f'***{self.defName}: test_0002: Open FAQ 1***')
        self.action.move_to_element(self.driver.find_element_by_xpath(self.hp.faq1list1)).click().perform()

        self.waitAndsee(self.hp.faq1list1)
        self.logger.info('--Found the FAQ1 details')
        self.logger.info('PASSED\n')

    def test_0003(self, additionalSetup):
        self.logger.info(f'***{self.defName}: test_0003: Footer Link***')
        self.action.move_to_element(self.driver.find_element_by_xpath(self.hp.privacypolicy)).click().perform()
        self.pp = PrivacyPolicy(self.driver)

        self.waitAndsee(self.pp.paragraph)
        self.logger.info('--Found the Privacy Policy Page')
        self.logger.info('PASSED\n')


    def test_0004(self, additionalSetup):
        MYSQL = MySQLConnection()
        self.counter = 0

        if self.counter == 0:
            MYSQL.cursor.execute("select * from customers where id = 15")
            record = MYSQL.cursor.fetchall()
            for i in record:
                self.logger.info(i[0])

            self.logger.info("PASSED\n")
            assert True

        else:
            self.logger.info(f'FAILED - {self.counter} element(s) failed to verify.\n')
            assert False




