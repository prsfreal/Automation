from selenium.webdriver.common.action_chains import ActionChains
import time


class federalLandingPage:

    startreportbutton = '//*[@id="post-3291"]/div/div/div/div/section[8]/div/div/div/div/div/div[3]/div/div/a/span/span'

    def __init__(self, driver):
        self.driver = driver
        self.action = ActionChains(self.driver)

    def navigateToPurchase(self):
        self.action.move_to_element(self.driver.find_element_by_xpath(self.startreportbutton))
        self.action.click(self.driver.find_element_by_xpath(self.startreportbutton))
        self.action.perform()
        time.sleep(1)