import time
from UTILITIES.BasicClassConfig import basic


class FederalCheckoutPage(basic):

    orderfirstname = '//*[@id="billing_first_name"]'
    orderlastname = '//*[@id="billing_last_name"]'
    orderaddress = '//*[@id="billing_address_1"]'
    ordercity = '//*[@id="billing_city"]'
    orderstate = '//*[@id="billing_state"]'
    orderzip = '//*[@id="billing_postcode"]'
    orderphone = '//*[@id="billing_phone"]'
    orderemail = '//*[@id="billing_email"]'
    ordercontractorname = '//*[@id="billing_contractors_name"]'
    ordercontractoremail = '//*[@id="billing_contractors_email_address"]'
    ordercouponcode = '//*[@id="coupon_code"]'
    orderccinfo = '/html/body/div[1]/div/div/div/section[2]/div/div/div/div/div/div/div/div/div/div/form/div[2]/div/div[2]/ul/li/div/div/fieldset/div[1]/div/iframe'
    orderbutton = '//*[@id="place_order"]'
    ordertccheckbox = '//*[@id="terms"]'
    addonorderbutton = '//*[@id="wcf-upsell-offer"]/span/span'

    def __init__(self, driver):
        self.driver = driver

    def makePurchase(self, user):
        self.driver.find_element_by_xpath(self.orderfirstname).clear()
        self.driver.find_element_by_xpath(self.orderfirstname).send_keys(user.firstname)
        self.driver.find_element_by_xpath(self.orderlastname).clear()
        self.driver.find_element_by_xpath(self.orderlastname).send_keys(user.lastname)
        self.driver.find_element_by_xpath(self.orderaddress).clear()
        self.driver.find_element_by_xpath(self.orderaddress).send_keys(user.address)
        self.driver.find_element_by_xpath(self.ordercity).clear()
        self.driver.find_element_by_xpath(self.ordercity).send_keys(user.city)
        self.driver.find_element_by_xpath(self.orderstate).clear()
        self.driver.find_element_by_xpath(self.orderstate).send_keys(user.state)
        self.driver.find_element_by_xpath(self.orderzip).clear()
        self.driver.find_element_by_xpath(self.orderzip).send_keys(user.zip)
        self.driver.find_element_by_xpath(self.orderphone).clear()
        self.driver.find_element_by_xpath(self.orderphone).send_keys(user.phone)
        self.driver.find_element_by_xpath(self.orderemail).clear()
        self.driver.find_element_by_xpath(self.orderemail).send_keys(user.email)
        self.driver.find_element_by_xpath(self.ordercontractorname).clear()
        self.driver.find_element_by_xpath(self.ordercontractorname).send_keys(user.contractorname)
        self.driver.find_element_by_xpath(self.ordercontractoremail).clear()
        self.driver.find_element_by_xpath(self.ordercontractoremail).send_keys(user.contractoremail)
        self.driver.find_element_by_xpath(self.ordercouponcode).clear()
        self.driver.find_element_by_xpath(self.ordercouponcode).send_keys(user.coupon)

        try:
            self.waitAndsee(self.orderccinfo)
            self.driver.switch_to.frame(frame_reference=self.driver.find_element_by_xpath(self.orderccinfo))
            self.driver.find_element_by_name('cardnumber').clear()
            self.driver.find_element_by_name('cardnumber').send_keys(user.ccnumber)
            self.driver.find_element_by_name('exp-date').send_keys(user.ccdate)
            self.driver.find_element_by_name('cvc').send_keys(user.cccode)
            self.driver.switch_to.default_content()

        except:
            self.logger.info(f'***{basic.defName}')
            self.logger.exception(f'--Could not locate ELEMENT by XPATH')
            self.logger.info(f'self.orderccinfo XPATH = {self.orderccinfo}\n')
            assert False

        try:
            self.waitAndsee(self.ordertccheckbox)
            time.sleep(3)
            self.driver.find_element_by_xpath(self.ordertccheckbox).click()
            self.driver.find_element_by_xpath(self.orderbutton).click()

        except:
            self.logger.info(f'***{basic.defName}')
            self.logger.exception(f'--Could not locate ELEMENT by XPATH')
            self.logger.info(f'self.ordertccheckbox XPATH = {self.ordertccheckbox}\n')
            assert False






