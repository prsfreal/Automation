from selenium.webdriver.common.action_chains import ActionChains
import time

class HomePage:

    account = '//*[@id="menu-item-3492"]/a'
    faq1 = '//*[@id="elementor-tab-title-9251"]/a'
    faq1list1 = '//*[@id="elementor-tab-content-9251"]/ul/li[1]'
    contactbutton = '//*[@id="post-2820"]/div/div/div/div/section[5]/div[2]/div/div[3]/div/div[2]/div[2]/div/div/a/span/span'
    slider1text = 'I had a contractor get hurt while on the job at my house. Good thing I verified they had liability insurance.'
    slider2text = 'So easy to use, no other product on the market is so consumer focused.'
    slider3text = 'I wanted to add a deck to my house and so many of the contractors turned out to not be insured. Validate Services helped me find a legitimate contractor.'
    privacypolicy = '//*[@id="menu-item-2351"]/a'

    def __init__(self, driver):
        self.driver = driver
        self.action = ActionChains(self.driver)

    def navigateToAccountPage(self):
        self.action.move_to_element(self.driver.find_element_by_xpath(self.account))
        self.action.click(self.driver.find_element_by_xpath(self.account))
        self.action.perform()
        time.sleep(1)





