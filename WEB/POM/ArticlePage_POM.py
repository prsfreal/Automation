from selenium.webdriver.common.action_chains import ActionChains
import time


class ArticlePage:

    twitterwidget = '//*[@id="main"]/div/div/section[2]/div/div/div/div/div/div[2]/div/div/div[2]'
    emailfield = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[1]/div[2]/form/div/div[1]/label/div/div[2]/div/input'
    passwordfield = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[1]/div[2]/form/div/div[2]/label/div/div[2]/div/input'
    loginbutton = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[2]/div[2]/div/span/span/span'
    tweetfield = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[3]/div/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div[1]/div/div/div/div[1]/div/div/div/div/div/div/div/div'
    discountemail = '//*[@id="form-field-newemail"]'
    discountname = '//*[@id="form-field-field_d5d4726"]'
    discountsubmit = '//*[@id="main"]/div/div/section[4]/div/div/div/div/div/div[2]/div/form/div/div[3]/button'
    discountverifypath = '//*[@id="main"]/div/div/section[4]/div/div/div/div/div/div[2]/div/form/div[2]'
    discountverifytext = 'You should receive your email with coupon shortly. Thank you'
    backgroundcheckbutton = '//*[@id="main"]/div/div/section[3]/div/div/div/div/div/div/div/div/div/div/section[2]/div/div/div/div/div/div[2]/div/div/a/span/span'

    def __init__(self, driver):
        self.driver = driver
        self.action = ActionChains(self.driver)

    def navigateToTwitter(self):
        self.action.move_to_element(self.driver.find_element_by_xpath(self.twitterwidget))
        self.action.click(self.driver.find_element_by_xpath(self.twitterwidget))
        self.action.perform()
        time.sleep(1)

    def signIntoTwitter(self, email, password):
        self.driver.find_element_by_xpath(self.emailfield).clear()
        self.driver.find_element_by_xpath(self.emailfield).send_keys(email)
        self.driver.find_element_by_xpath(self.passwordfield).clear()
        self.driver.find_element_by_xpath(self.passwordfield).send_keys(password)
        self.driver.find_element_by_xpath(self.loginbutton).click()

    def discountSubmit(self, email, password):
        self.driver.find_element_by_xpath(self.discountemail).clear()
        self.driver.find_element_by_xpath(self.discountemail).send_keys(email)
        self.driver.find_element_by_xpath(self.discountname).clear()
        self.driver.find_element_by_xpath(self.discountname).send_keys(password)
        self.driver.find_element_by_xpath(self.discountsubmit).click()

    def navigateToBackgroundCheck(self):
        self.action.move_to_element(self.driver.find_element_by_xpath(self.backgroundcheckbutton))
        self.action.click(self.driver.find_element_by_xpath(self.backgroundcheckbutton))
        self.action.perform()
        time.sleep(1)




